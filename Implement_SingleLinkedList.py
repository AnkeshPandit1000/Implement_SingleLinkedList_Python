#Implemenet a Single Linked List using classes

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LInkedList:
    def __init__(self):
        self.head = None
#printing the Linked List/ Traversal OPeration -->
    def printLL(self):
        if self.head == None:
            print("The Linked List is Empty")
        else:
            n = self.head
            while n.ref is not None:
                print(n.data)
                n = n.ref

 #Add at the begining of Linked LIst-->
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

#Add at the end of the Linked List-->
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

#Add after a perticular value in a Linked List -->
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if(x==n.data):
                break
            n = n.ref
        if n is None:
            print("That Value is not present in the Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

#Add before a perticular value in Linked List-->
    def add_before(self,data,x):
        if self.head == None:
            print("LInked LIst is Empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("That Node is NOt present in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


