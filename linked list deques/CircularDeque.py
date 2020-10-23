class CircularDeque:
    def __init__(self):
        self.deque = [None, None, None, None, None]
        self.front = -1
        self.rear = -1

    def is_full(self):
        if self.front == self.rear +1:
            return True
        elif self.front == 0 & self.rear == len(self.deque)-1:
            return True
    def is_empty(self):
        if self.front == -1 & self.rear==-1:
            return True

    def enqueue_rear(self, obj):
        if self.is_full() == True:
            self.resize_deque()
        if self.front == -1 & self.rear == -1:
            self.front = 0
            self.rear = 0
            self.deque[self.rear] = obj
        elif self.rear == len(self.deque) - 1:
            self.rear = 0
            self.deque[self.rear] = obj
        else:
            self.rear += 1
            self.deque[self.rear] = obj

    def enqueue(self, obj):
        if self.is_full() == True:
            self.resize_deque()
        if self.front ==-1 & self.rear==-1:
            self.front = 0
            self.rear = 0
            self.deque[self.front] = obj
        elif self.front == 0:
            self.front = len(self.deque)-1
            self.deque[self.front] = obj
        else:
            self.front -=1
            self.deque[self.front] = obj

    def deque_rear(self):
        if self.is_empty() == True:
            print("The dequeue is empty.")
        if self.front == self.rear:
            self.rear = self.front = -1
        elif self.rear == 0:
            self.rear = len(self.deque)-1
        else:
            self.rear -= 1

    def deque_front(self):
        if self.is_empty() == True:
            print("The dequeue is empty.")
        elif self.front == self.rear:
            self.rear=self.front = -1
        if self.front == len(self.deque)-1:
            self.front =0
        else:
            self.front += 1

    def get_first(self):
        return self.deque[self.front]

    def get_last(self):
        return self.deque[self.rear]

    def resize_deque(self):

    def display(self):
        i = self.front
        while i != self.rear:
            print(self.deque[i])
            i = (i+1)%len(self.deque)
        print(self.deque[self.rear])

CD = CircularDeque()
CD.enqueue(56)
CD.enqueue(34)
CD.enqueue_rear(48)
CD.enqueue(456)
CD.enqueue_rear(68)
CD.enqueue(58)
CD.display()


