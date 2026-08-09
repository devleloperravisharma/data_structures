class Queue:
    def __init__(self):
        self.list = []
        self.limit = int(input("how many documents would you like to print?"))


    def spaces_left_in_queue(self):
        return self.limit - len(self.list)

    def enqueue(self):
        if self.spaces_left_in_queue() > 0:
            document = input("Enter the document you want to print: ")
            self.list.append(document)
        else:
            print("There's no space left!")

    def queue_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def dequeue(self):
        if self.queue_empty():
            print("Nothing to print, the queue is empty.")
        else:
            document = self.list.pop(0)
            print("Printing " + document + "...")


object = Queue()

# User chooses the documents
for i in range(object.limit):
    object.enqueue()

# Print the documents in order
while not object.queue_empty():
    object.dequeue()