class Queue:
    def __init__(self, limit):
        self.list = []
        self.limit = limit
    def spaces_left_in_queue(self):
        global spaces_left
        spaces_left = self.limit - len(self.list)
        return len(self.list)
    def enqueue(self):
        if self.spaces_left_in_queue() < self.limit:
            ask = input("add a value!!")
            self.list.append(ask)
            print(self.list)
        else:
            print("there's no space left :( please delete an item!")
    def queue_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
    def dequeue(self):
        if self.queue_empty():
            print("nothing to delete in the list, add elements first")
        else:
            print(self.list.pop(0))
            print("first element deleted")
            print(self.list)

object = Queue(10)

# functions
object.spaces_left_in_queue()
object.queue_empty()

for i in range(10):
    object.enqueue()

object.enqueue()
object.dequeue()