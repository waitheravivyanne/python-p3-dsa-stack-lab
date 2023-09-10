class Stack:
    def __init__(self, items = [], limit = 100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
       if not self.full():
            self.items.append(item)   

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() >= self.limit

    def search(self, target):
          if target in self.items:
            return self.size() - self.items.index(target) - 1
          return -1
    
    #Bonus Questions
class TestStack:
    def test_init(self):
        stk = Stack([1, 2, 3, 4, 5], 10)
        expected = [1, 2, 3, 4, 5]
        assert all(expected[index] == stk.items[index] for index in range(len(expected)))
        assert stk.limit == 10

    def test_push(self):
        stk = Stack([1, 2, 3, 4, 5], 6)
        stk.push(6)
        assert stk.size() == 6
        assert stk.full()

        try:
            stk.push(7)
        except Exception as e:
            assert str(e) == "Stack is full"

    def test_size(self):
        stk = Stack([1, 2, 3, 4, 5], 10)
        assert stk.size() == 5

    def test_empty(self):
        stk = Stack()
        assert stk.isEmpty()

        stk.push(1)
        assert not stk.isEmpty()

        stk.pop()
        assert stk.isEmpty()

    def test_full(self):
        stk = Stack([1, 2, 3, 4, 5], 5)
        assert stk.full()

        stk.pop()
        assert not stk.full()

    def test_search(self):
        stk = Stack([5, 6, 7, 8, 9, 10], 10)
        assert stk.search(5) == 5
        assert stk.search(6) == 4
        assert stk.search(7) == 3
        assert stk.search(8) == 2
        assert stk.search(9) == 1
        assert stk.search(10) == 0
        assert stk.search(15) == -1


test = TestStack()
test.test_init()
test.test_push()
test.test_size()
test.test_empty()
test.test_full()
test.test_search()