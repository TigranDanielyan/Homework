class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur=cur.next

    def add_first(self,data):
        if self.head == None:
            new_node= Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head= new_node

    def add_last(self,data):
        if self.tail == None:
            new_node = Node(data)
            self.tail = new_node
            self.head = new_node
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_first(self):
        if self.head == None:
            print("The list is empty. Nothing to remove")
        elif self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head =self.head.next
            self.head.prev=None

    def remove_last(self):
        if self.tail == None:
            print("The list is empty. Nothing to remove")

        elif self.tail.prev == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def insert_after(self,new_data, target_data):
        cur = self.head
        found = False
        while cur:
            if cur.data != target_data:
                cur = cur.next
            else:
                found = True
                break
        if cur == self.tail:
            self.add_last(new_data)
        elif found == True:
            new_node = Node(new_data)
            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node
        else:
            print("Your target data is not in the list")

    def insert_before(self,new_data,target_data):
        cur = self.head
        found  = False
        while cur:
            if cur.data != target_data:
                cur = cur.next
            else:
                found = True
                break
        if cur == self.head:
            self.add_first()
        elif found == True:
            new_node = Node(new_data)
            cur.prev.next = new_node
            new_node.prev =cur.prev
            new_node.next = cur
        else:
            print("Your target data is not in the list")

    def first(self):
        return self.head.data


    def last(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        return cur.data

    def arrange(self):
        listOdd=[]
        listEven=[]
        if self.head == None:
            return None
        odd = self.head
        even =self.head.next
        while odd!= None and even!=None and odd.next !=None:
            listOdd.append(odd.data)
            listEven.append(even.data)
            odd = even.next
            even=odd.next
        print(listEven)
        print(listOdd)


dll = DoubleLinkedList()

dll = DoubleLinkedList()
dll.add_first(23)
dll.add_last(45)
dll.add_last(44)
dll.add_first(423)
dll.print_list()
dll.remove_first()
dll.insert_after(444,44)
dll.print_list()