class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == [] 

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    
