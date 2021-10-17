import queue

# data_queue = queue.Queue()
#
# data_queue.put("123123")
# data_queue.put(789456)
# print(data_queue.qsize())
# print(data_queue.get())
# print(data_queue.qsize())
# print(data_queue.get())
# print(data_queue.qsize())
#
# lifo = queue.LifoQueue() # last in first out
# lifo.put("qqqq")
# lifo.put(1234)
# print(lifo.qsize())
# print(lifo.get())
# print(lifo.qsize())
# print(lifo.get())
#
# pri = queue.PriorityQueue()
# pri.put((1,"어"))
# pri.put((2,"ㅇㅇ"))
# pri.put((5,"4124124"))
# pri.put((0.1,"22222"))
# print(pri.qsize())
# print(pri.get())
# print(pri.qsize())
# print(pri.get())
# print(pri.qsize())
# print(pri.get())
# print(pri.qsize())
# print(pri.get())

que = list()
def enqueue(data):
    que.append(data)
def dequeue():
    data = que[0]
    del que[0]
    return data

for i in range(10):
    enqueue(i)
print(que)
print(len(que))
print(dequeue())
print(que)
print(dequeue())
print(que)
print(dequeue())