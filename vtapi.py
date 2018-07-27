#!/usr/bin/env python
from requests import get, post
from queue import Queue
from threading import Thread, BoundedSemaphore, Timer

waiting_requests = Queue()
api_slots = BoundedSemaphore(value = 4)

def send_request():
	api_slots.acquire()
	request_info = waiting_requests.get()
	response = request_info.type(url, params = request_info.params)
	# spawn callback thread?
	Timer(60, api_slots.release).start()

Thread(target = send_request, name = 'Request Dispatcher', daemon=True).start()

