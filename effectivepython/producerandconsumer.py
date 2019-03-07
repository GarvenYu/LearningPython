#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import Queue
from threading import Thread

"""
Edition one
"""
# produce_queue = Queue()
#
#
# def consume():
#     print("consume waiting...")
#     produce_queue.get()
#     print("consume done...")
#     produce_queue.task_done()
#
#
# Thread(target=consume).start()
# produce_queue.put(object())
# print("produce waiting...")
# produce_queue.join()


"""
Edition two
"""


class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            # 阻塞直到队列非空
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                # 通知
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self, behavior, in_queue, out_queue):
        super().__init__()
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.behavior = behavior

    def run(self):
        for item in self.in_queue:
            print(self.behavior, str(item))
            self.out_queue.put(item)


init_queue = ClosableQueue()
work_queue = ClosableQueue()
done_queue = ClosableQueue()

threads = [StoppableWorker("work", init_queue, work_queue), StoppableWorker("check", work_queue, done_queue)]
for t in threads:
    t.start()
for item in range(10):
    init_queue.put(item)
init_queue.close()
init_queue.join()
work_queue.close()
work_queue.join()
print(done_queue.qsize(), 'items finished')
