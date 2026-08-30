class Queue:
    def __init__(self, limit):
        self.list = []
        self.limit = limit

    def spaces_left_in_queue(self):
        spaces_left = self.limit - len(self.list)
        return spaces_left

    def queue_full(self):
        if self.spaces_left_in_queue() == 0:
            return True
        else:
            return False

    def enqueue(self):
        if self.queue_full():
            print("There's no space left in the queue :(")
        else:
            ask = input("Add a value!! ")
            self.list.append(ask)
            print(self.list)

    def queue_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def dequeue(self):
        if self.queue_empty():
            print("Nothing to delete in the queue, add elements first")
        else:
            print(self.list.pop(0))
            print("First element deleted")
            print(self.list)


# positional argument - 10 is the limit
object = Queue(10)

# functions
object.spaces_left_in_queue()
object.queue_empty()

# Add elements until queue is full
for i in range(10):
    object.enqueue()

# Try to add another element
object.enqueue()

# Delete the first element
object.dequeue()
