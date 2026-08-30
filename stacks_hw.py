class Stack:
    def __init__(self, limit):
        # init = initialize properties of class
        self.list = []
        self.limit = limit

    def spaces_left_in_stack(self):
        spaces_left = self.limit - len(self.list)
        return spaces_left

    def stack_full(self):
        if self.spaces_left_in_stack() == 0:
            return True
        else:
            return False

    def add_more(self):
        if self.stack_full():
            print("There's no space left in the stack.")
        else:
            ask = input("Add a value: ")
            self.list.append(ask)
            print(self.list)

    def delete_elements(self):
        if len(self.list) == 0:
            print("Nothing to delete, sorry!!")
        else:
            del self.list[-1]
            print("Last element deleted")
            print(self.list)


# positional argument - 5 is the limit
object = Stack(5)

object.spaces_left_in_stack()
object.stack_full()

for i in range(5):
    object.add_more()

object.add_more()

object.delete_elements()
