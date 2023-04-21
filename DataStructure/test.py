import queue

data_queue = queue.PriorityQueue()

data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))

print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())