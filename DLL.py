class node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
        
class DLL:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("doubly link list is empty!")
        else:
            temp = self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp = temp.next
                
    def insert_begin(self,data):
        new_node = node(data)
        temp = self.head
        temp.prev = new_node
        new_node.next = temp
        self.head = new_node
        
    def insert_end(self,data):
        new_node = node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.next = None  
        
    def insert_position(self,pos,data):
        new_node = node(data)
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        
    def delete_begin(self):
        temp = self.head 
        self.head = temp.next
        temp.next.prev = None
        temp.next = None
        
    def delete_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
        temp.prev = None
        
    def delete_position(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.prev = prev
        
        
        
dl = DLL()
n = node(10)
dl.head = n
n1 = node(20)
n.next = n1
n1.prev = n
n2 = node(30)
n1.next = n2
n2.prev = n1
n3 = node(40)
n2.next = n3
n3.prev = n2
dl.insert_begin("rvn")
dl.insert_end("ayra")
dl.insert_position(3,"vandy")
dl.delete_begin()
dl.delete_end()
dl.delete_position(2)
dl.display()