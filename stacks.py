class Stack:
    def __init__(self, limit):
        #init = initialize properties of class
        self.list = []
        self.limit = limit
    def spaces_left_in_stack(self):
        spaces_left = self.limit - len(self.list)
        return spaces_left
    def stack_empty(self):
        if self.spaces_left_in_stack() == 0:
            return True
        else:
            return False
    def add_more(self):
        if self.spaces_left_in_stack() < self.limit:
            ask = print(input("add a value."))
            self.list.append(ask)
            print(self.list)
        else:
            print("there's no space left in the stack. please delete some elements necessary")
            
# positional argument - expecting something in function, where you have to give value. "20" is a positional argument for the limit. all dependent on parameter
object = Stack(20)
