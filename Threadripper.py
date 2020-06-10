# -*- coding: utf-8 -*-

import multiprocessing, math, threading, time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


class Threadripper:
	def __init__(self, process_num=0, thread_num=0):
		self.cpu_count = multiprocessing.cpu_count()
		self.thread_num = thread_num if thread_num > 0 else self.cpu_count
		self.process_num = process_num if process_num > 0 else self.cpu_count

	def list_split(self, items):
		res = []
		length = len(items)
		n = length if length < self.cpu_count else self.cpu_count

		for i in range(n):
			item = items[math.floor(i/n*length):math.floor((i+1)/n*length)]
			res.append(item)
		return res

	def thread_pool(self, func, data):
		threadExecutor = ThreadPoolExecutor(self.thread_num)
		for d in data:
			threadExecutor.submit(func, d)


	def ripper(self, data_list, func):
		processExecutor = ProcessPoolExecutor(self.process_num)
		split_data = self.list_split(data_list)
		print(split_data)
		for data in split_data:
			processExecutor.submit(self.thread_pool, func, data)

def test_do(d):
	print(threading.currentThread().name)

if __name__ == "__main__":
	p = Threadripper()
	data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	p.ripper(data, do)