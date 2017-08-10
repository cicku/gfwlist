#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of GFWList.
#
# Copyright (C) 2017 GFWList Project

"""
Batch processing of FTChinese URLs for GFWList project.
Sample URL: http://www.ftchinese.com/story/0010XXXXX
"""
import os
import sys
import urllib
import requests

from argparse import ArgumentParser

'''
Argparser for usage ./ftchinese.py seqEnd
'''
def parser_args():
    parser = ArgumentParser(description='Detect FTChinese URLs and find out those blocked.')
    parser.add_argument("seqEnd", type=int, default='1073715', help='Read input number as the end of the sequence')
    return parser.parse_args()

'''
Generate a list full of newID in order to add filters for test.
'''
def genIDSeq(seqEnd):
    for i in range(1000001, seqEnd):
        yield(i)

def main():
    args = parser_args()
    data = genIDSeq(args.seqEnd)
    with open('newID.txt', 'w') as fID:
        for j in data:
            fID.write(str(j).zfill(9) + '\n')

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 2 :
        print('\nRange of newsID is missing. Use option -h to check for help. Exiting......')
        sys.exit(1)
    main()