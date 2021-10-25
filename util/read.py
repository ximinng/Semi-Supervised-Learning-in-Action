# -*- coding: utf-8 -*-
"""
   Project : Semi-Supervised-Learning-in-Action
   File :  read.py
   Description : 
   Author : xingximing.xxm
   Date : 2021/10/25 1:15 PM 
"""
import yaml


def over_write_args_from_file(args, yml):
    if yml == '':
        return
    with open(yml, 'r', encoding='utf-8') as f:
        dic = yaml.load(f.read(), Loader=yaml.Loader)
        for k in dic:
            setattr(args, k, dic[k])
