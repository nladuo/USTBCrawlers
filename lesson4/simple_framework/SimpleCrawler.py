# coding=utf8
""" 简易爬虫框架 """
from multiprocessing import Manager, Pool


class SimpleCrawler:
    def __init__(self, c_num):
        self.task_queue = Manager().Queue()  # 任务队列
        self.workers = {}                    # Worker, 字典类型, 存放不同的Worker
        self.c_num = c_num                   # 并发数,开几个进程

    def add_task(self, task):
        self.task_queue.put(task)

    def add_worker(self, identifier, worker):
        self.workers[identifier] = worker

    def start(self):
        pool = Pool(self.c_num)
        while True:
            task = self.task_queue.get(True)
            if task['id'] == "NO":  # 结束爬虫
                pool.close()
                pool.join()
                exit(0)
            else:  # 给worker完成任务
                worker = self.workers[task['id']]
                pool.apply_async(worker, args=(self.task_queue, task))
