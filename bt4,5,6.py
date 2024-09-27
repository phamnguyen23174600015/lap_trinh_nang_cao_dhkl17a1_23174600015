
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:  
            return self.items.pop()
        else:
            return "stack trống"

    def peek(self):
        if len(self.items) > 0:  
            return self.items[-1]
        else:
            return "Trống"

    def size(self):
        return len(self.items)
    

    def print_stack(self):
        if len(self.items) == 0:
            print("Stack trống.")
        else:
            print("Nd trong stack:")
            for item in self.items:
                print(item)

    
stack = Stack()

stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Top element:", stack.peek())

popped_item = stack.pop()
print("\nPopped item:", popped_item)

print("Stack size:", stack.size())

stack.print_stack()