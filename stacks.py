class Stack:
    def __init__(self, limit):
        #init = initialize properties of class
        self.list = []
        self.limit = limit
    def spaces_left_in_stack(self):
        spaces_left = self.limit - len(self.list)
        return spaces_left
# positional argument - expecting something in function, where you have to give value. "20" is a positional argument for the limit. all dependent on parameter
object = Stack(20)
