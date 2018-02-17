#!/usr/bin/env python
# coding=utf8
""" 多进程的使用 """
import multiprocessing
import time
import os


def process(process_id):
    while True:
        time.sleep(1)
        print 'Task %d, pid: %d, doing something' % (process_id, os.getpid())

if __name__ == "__main__":
    # 进程1
    p = multiprocessing.Process(target=process, args=(1,))
    p.start()

    # 进程2
    p2 = multiprocessing.Process(target=process, args=(2,))
    p2.start()
