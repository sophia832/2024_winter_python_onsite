class stack():
    def_init_(self, *args):
        self.stack.items = [arg for arg in args]

    def peek(self):
        if len(self.stack_items) > 0:
            return self.stack_items[-1]
        else:
            return None

    def pop(self):
        if len(self.stack_items) > 0:
            return self.stack_items.pop()
        else:
            return None

    def push(self):
        if len(self.stack_items) > 0:
            return self.stack_items.push()
        else:
            return None

    def size(self):
        if len(self.stack_items) > 0:
            return self.stack_items.size()
        else:
            return None


# Linked stack

class linkedStack():
    def push(self, data):
        current = stackNode(data, next=self.top)
        self.top = current

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data

    def pop(self):
        if self.top is None:
            return None
        else:
            pop_item = self.top
            self.top = pop_item.next
            return

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
