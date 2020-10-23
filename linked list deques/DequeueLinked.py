class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedDequeue:

    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur=cur.next

    def add_fist(self,data):
        if self.head == None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head= new_node

    def add_last(self,data):
        if self.head == None:
            new_node = Node(data)
            new_node.prev =None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def remove_last(self):
        if self.head == None:
            print("The list is empty. Nothing to remove")
        else:
            if self.head.next!=None:
                cur =self.head
                while cur.next != None:
                    cur = cur.next
                cur.prev.next = None
            else:
                self.head = None

    def remove_first(self):
        if self.head == None:
            print("The list is empty. Nothing to remove")
        else:
            self.head =self.head.next
            self.head.prev=None

    def first(self):
        return self.head.data


    def last(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        return cur.data

ld = LinkedDequeue()
print('1st list')
ld.add_fist(55)
ld.add_last(45)
ld.print_list()
ld.remove_last()
print('2nd list')
ld.add_fist(55)
ld.add_last(45)
ld.remove_first()
ld.print_list()

