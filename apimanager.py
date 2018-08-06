#!/usr/bin/env python
from requests import get, post
from queue import Queue
from threading import BoundedSemaphore, Timer

class BaseApi:
	"""docstring for BaseApi"""
	def __init__(self, base_url, rate, interval):
		super(BaseApi, self).__init__()
		self.base_url = base_url
		self.interval = interval
		self.api_slots = BoundedSemaphore(value = rate)
		self.waiting_requests = Queue()

	def send_requests(self):
		self.api_slots.acquire()
		request_info = self.waiting_requests.get()
		response = request_info.method(self.base_url + request_info.url, params = request_info.params)
		# spawn callback thread?
		Timer(self.interval, self.api_slots.release).start()

class RequestInfo:
	"""docstring for RequestInfo"""
	def __init__(self, method, url, params):
		method = method.lower().trim()

		if method == 'get':
			self.method = get
		elif method == 'post':
			self.method = post

		self.url = url
		self.params = params
		

