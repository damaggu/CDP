# ----------------------------------------
# Written by Yude Wang
# ----------------------------------------
import torch
import argparse
import os
import sys
import cv2
import time


class ModelConfiguration():
    def __init__(self):
        # TODO come up with more elegant way to do this # os.path.abspath(os.path.join(os.path.dirname("__file__")))
        self.MODEL_NAME = 'deeplabv3plus'
        self.MODEL_BACKBONE = 'res101_atrous'
        self.MODEL_OUTPUT_STRIDE = 16
        self.MODEL_ASPP_OUTDIM = 256
        self.MODEL_SHORTCUT_DIM = 48
        self.MODEL_SHORTCUT_KERNEL = 1
        self.MODEL_NUM_CLASSES = 21
        self.BN_MOM = 0.0003

    #     self.__check()
    #     self.__add_path(os.path.join(self.ROOT_DIR, 'lib'))
    #
    # def __check(self):
    #     if not torch.cuda.is_available():
    #         raise ValueError('config.py: cuda is not avalable')
    #     if self.TRAIN_GPUS == 0:
    #         raise ValueError('config.py: the number of GPU is 0')
    #     # if self.TRAIN_GPUS != torch.cuda.device_count():
    #     #	raise ValueError('config.py: GPU number is not matched')
    #     if not os.path.isdir(self.LOG_DIR):
    #         os.makedirs(self.LOG_DIR)
    #     if not os.path.isdir(self.MODEL_SAVE_DIR):
    #         os.makedirs(self.MODEL_SAVE_DIR)
    #
    # def __add_path(self, path):
    #     if path not in sys.path:
    #         sys.path.insert(0, path)


cfg = ModelConfiguration()
