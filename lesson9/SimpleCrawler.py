""" 简易爬虫框架 """
from multiprocessing import Manager, Pool


class SimpleCrawler:
    def __init__(self, c_num):
        self.task_queue = Manager().Queue()

        self.workers = {}
        self.c_num = c_num

    def add_task(self, task):
        self.task_queue.put(task)

    def add_worker(self, identifier, parser):
        self.workers[identifier] = parser

    def start(self):
        pool = Pool(self.c_num)
        lock = Manager().Lock()
        while True:
            task = self.task_queue.get(True)
            if task['id'] == "NO":  # 结束
                pool.close()
                pool.join()
                exit(0)
            else:  # 下载页面
                worker = self.workers[task['id']]
                pool.apply_async(worker, args=(self.task_queue, task, lock))
