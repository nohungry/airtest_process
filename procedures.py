from abc import ABCMeta, abstractclassmethod

# 抽象base層級 for 整個流程操作
class procedures(object, metaclass=ABCMeta):
    def __init__(self, device, path, sign):
        self.device = device
        self.path = path
        self.sign = sign

    @abstractclassmethod
    def universal(self):
        pass
    
