import queue


queue=queue.Queue()
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
