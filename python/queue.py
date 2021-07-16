
class Queue():
	def __init__(self):
		self.queue = []
		self.size = 3

	def enqueue(self, element):
		if self.is_full():
			print("Queue is full")
			return
		self.queue.insert(0, element)

	def dequeue(self):
		if self.is_empty():
			print("Queue is empty")
			return
		return self.queue.pop()


	def peek(self):
		if self.is_empty():
			print("Queue is empty")
			return
		index = len(self.queue) - 1
		return self.queue[index]


	def is_full(self):
		return len(self.queue) > self.size - 1


	def is_empty(self):
		return len(self.queue) == 0



s = Queue()
s.enqueue(10)
print("enqueue = ", 10)
s.enqueue(20)
print("enqueue = ", 20)
s.enqueue(30)
print("enqueue = ", 30)

element = s.dequeue()
print("\ndequeue = ", element)

element = s.peek()
print("peek = ", element)
