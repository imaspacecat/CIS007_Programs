class Stack(list):
    def __init__(self):
        super().__init__()

    def isEmpty(self):
        return super().__len__() == 0

    def peek(self):
        return super()[super().__len__()-1]

    def push(self, value):
        super().append(value)

    def pop(self):
        return super().pop(super().__len__()-1)

    def getSize(self):
        super().__len__()

s = Stack()
for i in range(5):
    val = input("Enter a string: ")
    s.push(val)


while not s.isEmpty():
    print(s.pop())