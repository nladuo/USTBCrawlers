#!/usr/bin/env python
# coding=utf8

from multiprocessing import Process, Queue
import time


def produce(q):  # 生产
    for i in range(10000):
        print "Produce ", i
        q.put(i)


def consume(q):  # 消费
    while True:
        if not q.empty():
            value = q.get(True)
            print 'Consumer 1, Get %s from queue.' % value
            time.sleep(1)


def consume2(q):  # 消费
    while True:
        if not q.empty():
            value = q.get(True)
            print 'Consumer 2, Get %s from queue.' % value
            time.sleep(1)


if __name__ == '__main__':
    q = Queue(5)    # 队列最多放5个数据, 超过5个则会阻塞住
    producer = Process(target=produce, args=(q,))
    consumer = Process(target=consume, args=(q,))
    consumer2 = Process(target=consume2, args=(q,))
    
    producer.start()
    consumer.start()
    consumer2.start()

    producer.join()  # 等待结束, 死循环使用Ctrl+C退出
    consumer.join()
    consumer2.join()
