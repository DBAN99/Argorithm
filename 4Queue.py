import queue

data_queue = queue.Queue()

data_queue.put("123123")
data_queue.put(789456)
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())