""" 进程池的使用 """
from multiprocessing import Pool
import time
import os


def do_something(num):
    for i in range(2):
        time.sleep(1)
        print("doing %d, pid: %d" % (num, os.getpid()))

if __name__ == '__main__':
    p = Pool(3)
    for page in range(1, 11):  # 10个任务
        p.apply_async(do_something, args=(page,))

    p.close()   # 关闭进程池, 不再接受任务
    p.join()    # 等待子进程结束
