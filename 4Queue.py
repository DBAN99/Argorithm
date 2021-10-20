import queue

nomal = queue.Queue()

# nomal.put("123")
# nomal.put("456")
# print(nomal.qsize())
# print(nomal.get())
# print(nomal.qsize())
# print(nomal.get())
#
#
# lifo = queue.LifoQueue() # last in first out
# lifo.put("디반블로그")
# lifo.put(123)
# print(lifo.qsize())
# print(lifo.get())
# print(lifo.qsize())
# print(lifo.get())


pri = queue.PriorityQueue()

pri.put((1,"녕"))
pri.put((2,"하"))
pri.put((5,"요"))
pri.put((0.1,"안"))
pri.put((3,"세"))
a = pri.qsize()

for i in range(a):
    print(pri.get())

#
# que = list()
# def enqueue(data):
#     que.append(data)
# def dequeue():
#     data = que[0]
#     del que[0]
#     return data
#
# for i in range(10):
#     enqueue(i)
# print(que)
# print(len(que))
# print(dequeue())
# print(que)
# print(dequeue())
# print(que)
# print(dequeue())