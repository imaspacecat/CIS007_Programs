class Test:
    def __init__(self, i = 1, j = 1):
        self.i = i
        self.j = j

    def __str__(self):
        return "Done"

    def __eq__(self, other):
        return self.i * self.j == other.i * other.j

def main():
    t1 = Test(2, 3)
    t2 = Test(1, 6)
    print(t1 == t2)

main()