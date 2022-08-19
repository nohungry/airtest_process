import logging
import cv2
import os
import copy
import logging

from airtest.utils.logger import get_logger
from datetime import datetime

from airtest.aircv.error import * # noqa
from airtest.aircv.utils import check_image_valid, generate_result, print_run_time
from airtest.aircv.keypoint_base import KeypointMatching


LOGGING = get_logger(__name__)

class KAZEMatching(KeypointMatching):
    """
        特徵點辨識: KAZE.
    """
    # 參數: FILTER_RATIO是SIFT優秀特徵點過濾比例值
    FILTER_RATIO = 0.59

    def __init__(self, im_search, im_source, threshold=0.5, rgb=True):
        # super(KeypointMatching, self).__init__()
        super().__init__(im_search, im_source)
        self.threshold = threshold
        self.rgb = rgb

    @print_run_time
    def find_best_result(self, draw=False):
        # 基於KAZE進行圖像辨識, 只篩選出最優區域.
        # step01. confirm image current
        if not check_image_valid(self.im_source, self.im_search):
            return None

        # step02. 獲取特徵點集同時matching特徵點: return good, pypts, kp_sch, kp_src
        self.kp_sch, self.kp_src, self.good = self._get_key_points()

        # step03. according to keypoint[good], extraction image area:
        if len(self.good) in [0, 1]:
            # if keypoint = 0, 無法提取識別區域;
            # if keypoint = 1, 無法獲取目標區域;
            return None
        elif len(self.good) in [2, 3]:
            # keypoint = 2 or 3, 根據點對求出目標區域, 計算出信任度.
            if len(self.good) == 2:
                origin_result = self._handle_two_good_points(self.kp_sch, self.kp_src, self.good)
            else:
                origin_result = self._handle_three_good_points(self.kp_sch, self.kp_src, self.good)
            # 某些特殊情況下直接返回None作為匹配結果:
            if origin_result is None:
                return origin_result
            else:
                middle_point, pypts, w_h_range = origin_result
        else:
            # keypoint >= 4, 使用單矩陣映射求出目標區域, 計算出信任度.
            middle_point, pypts, w_h_range = self._many_good_pts(self.kp_sch, self.kp_src, self.good)

        # step04. 根據識別區域, 求出信任度, 回傳結果
        x_min, x_max, y_min, y_max, w, h = w_h_range
        target_img = self.im_source[y_min:y_max, x_min:x_max]
        resize_img = cv2.resize(target_img, (w, h))
        confidence = self._cal_confidence(resize_img)

        best_match = generate_result(middle_point, pypts, confidence)
        LOGGING.warning("[KAZE] threshold=%s, result=%s" % (self.threshold, best_match))
        if draw == True:
            self.draw_keypoint(middle_point)
        
        if confidence >= self.threshold:
            return best_match, confidence
        else:
            return None
        # return best_match if confidence >= self.threshold else None

    def draw_keypoint(self, middle_point):
        nowTime = datetime.today().strftime("%Y%m%d_%H%M%S")
        desktop = os.path.join(os.path.expanduser("~"), "Desktop") + "\\"
        logFolderPath = os.path.join(desktop, r"image_Log")
        if not os.path.exists(logFolderPath):
            os.mkdir(logFolderPath)
        logImage = os.path.join(logFolderPath, r"image_" + nowTime + ".jpg")
        imageInit = copy.deepcopy(self.im_source)
        # 紅色色碼
        color = (0, 0, 255)
        cv2.circle(imageInit, middle_point, 20, color, 5)
        cv2.imwrite(logImage, imageInit)

    def init_detector(self):
        self.detector = cv2.SIFT_create(edgeThreshold=10)

        # create FlnnMatcher object:
        self.matcher = cv2.FlannBasedMatcher({'algorithm': 0, 'trees': 5}, dict(checks=50))

    def get_keypoints_and_descriptors(self, image):
        """獲取圖像特徵點和描述符."""
        keypoints, descriptors = self.detector.detectAndCompute(image, None)
        return keypoints, descriptors
    
    def match_keypoints(self, des_sch, des_src):
        """Match descriptors (特徵值匹配)."""
        return self.matcher.knnMatch(des_sch, des_src, k=2)
    
    def _get_key_points(self):
        self.init_detector()
        kp_sch, des_sch = self.get_keypoints_and_descriptors(self.im_search)
        kp_src, des_src = self.get_keypoints_and_descriptors(self.im_source)
        if len(kp_sch) < 2 or len(kp_src) < 2:
            raise NoMatchPointError("Not enough feature points in input images !")
        matches = self.match_keypoints(des_sch, des_src)

        good = []
        for m, n in matches:
            if m.distance < self.FILTER_RATIO * n.distance:
                good.append(m)

        good_diff, diff_good_point = [], [[]]
        for m in good:
            diff_point = [int(kp_src[m.trainIdx].pt[0]), int(kp_src[m.trainIdx].pt[1])]
            if diff_point not in diff_good_point:
                good_diff.append(m)
                diff_good_point.append(diff_point)
        good = good_diff

        return kp_sch, kp_src, good