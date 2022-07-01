import cv2
import os
import copy

from airtest.utils.logger import get_logger
from datetime import datetime

from airtest.aircv.utils import check_image_valid, generate_result
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
        super().__init__()
        self.im_source = im_source
        self.im_search = im_search
        self.threshold = threshold
        self.rgb = rgb

    def find_best_result(self):
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
        LOGGING.debug("[KAZE] threshold=%s, result=%s" % (self.threshold, best_match))
        self.draw_keypoint(middle_point)

        return best_match if confidence >= self.threshold else None

    def draw_keypoint(self, middle_point):
        nowTime = datetime.today().strftime("%Y%m%d_%H%M%S")
        desktop = desktop = os.path.join(os.path.expanduser("~"), "Desktop") + "\\"
        logFolderPath = os.path.join(desktop, r"image_Log")
        if not os.path.exists(logFolderPath):
            os.mkdir(logFolderPath)
        logImage = os.path.join(logFolderPath, r"image_" + nowTime + ".jpg")
        imageInit = copy.deepcopy(self.im_source)
        # 紅色色碼
        color = (0, 0, 255)
        cv2.circle(imageInit, middle_point, 20, color, 5)
        cv2.imwrite(logImage, imageInit)