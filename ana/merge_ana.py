'''
Author: dochengzz
Date: 2023-11-08 22:01:56
LastEditTime: 2023-11-08 22:03:11
LastEditors: dochengzz
Description: 
FilePath: /pyskl/ana/merge_ana.py
'''

from mmcv import load, dump
from pyskl.smp import *


os.chdir('/ana')
train = load('my_dataset.json')
annotations = load('fitness_annos.pkl')
split = dict()
split['train'] = [x['vid_name'] for x in train]
# split['test'] = [x['vid_name'] for x in test]
dump(dict(split=split, annotations=annotations), 'fitness.pkl')