'''
Author: dochengzz
Date: 2023-11-08 21:59:16
LastEditTime: 2023-11-08 22:02:41
LastEditors: dochengzz
Description: 
FilePath: /pyskl/ana/gengerate_list.py
'''
from mmcv import load, dump
from pyskl.smp import *
train = load('my_dataset.py')
# test = load('Diving48_V2_test.json')
tmpl = 'rgb/{}.mp4'

lines = [(tmpl + ' {}').format(x['vid_name'], x['label']) for x in train + test]
mwlines(lines, 'fitness.list')

os.chdir('..')

