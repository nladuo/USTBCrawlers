#!/usr/bin/env python
# coding=utf8
""" 多进程的使用 """
import multiprocessing
import time
import os


def process(process_id):
    time.sleep(3)
    print 'Process %d, pid: %d' % (process_id, os.getpid())

p = multiprocessing.Process(target=process, args=(1,))
p.start()

p2 = multiprocessing.Process(target=process, args=(2,))
p2.start()

