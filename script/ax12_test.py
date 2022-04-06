#!/usr/bin/env python
# coding=UTF-8
'''
Author: Wei Luo
Date: 2022-04-06 16:14:49
LastEditors: Wei Luo
LastEditTime: 2022-04-06 16:16:54
Note: Note
'''

from ax12a_itm import AX12AMotorController
import time

if __name__ == '__main__':
    obj = AX12AMotorController()
    time.sleep(2)
    obj.movePosition(1, 511)
    time.sleep(2)
    obj.movePosition(1, 600)
    time.sleep(2)
    obj.movePosition(1, 400)
