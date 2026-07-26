class Stack:
    def __init__(self, limit):
        #init = initialize properties of class
        self.list = []
        self.limit = limit
    def spaces_left_in_stack(self):
        spaces_left = self.limit - len(self.list)
        return len(self.list)
    def stack_empty(self):
        if self.spaces_left_in_stack() == 0:
            return True
        else:
            return False
    def add_more(self):
        if self.spaces_left_in_stack() < self.limit:
            ask = input("add a value.")
            self.list.append(ask)
            print(self.list)
        else:
            print("there's no space left in the stack. please delete some elements necessary")
    def delete_elements(self):
        if self.stack_empty():
            print("nothing to delete, sorry !!")
        else:
            print(self.list.pop())
            print("element deleted")
            print(self.list)
# positional argument - expecting something in function, where you have to give value. "20" is a positional argument for the limit. all dependent on parameter
object = Stack(20)
object.spaces_left_in_stack()
object.stack_empty()
for i in range(20):
    object.add_more()
object.add_more()
object.delete_elements()