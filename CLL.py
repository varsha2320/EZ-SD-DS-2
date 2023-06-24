class Node:
    def _init_(self,data):
        self.data=data
        self.next=None

class Cll:
    def _init_(self):
        self.head=None
        self.tail=None

    def display(self):
        if self.head is None:
            print("Circular list is empty")
        else:
            temp=self.head
            print(temp.data,"->",end="")            
            while (temp.next!=self.head):
                temp=temp.next
                print(temp.data,"->",end="")
            print(temp.next.data)
                
    def insert_beg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
                        
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head

        else:
            self.tail.next=new_node
            self.tail=new_node
            self.tail.next=self.head

    '''def insert_mid(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node'''

    def insert_pos(self,pos,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            if pos==1:
                insert_beg(data)
            else:
                temp = self.head
                for i in range(1,pos-1):
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node

    def delete_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.tail.next=self.head
        
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next!=self.head:
            temp=temp.next
            prev=prev.next
        temp.next=None
        self.tail=prev
        self.tail.next=self.head
        
    '''def delete_pos(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None'''

    def delete_pos(self,pos):
        if self.head is None:
            print("CLL is empty")
        elif pos == 1:
            delete_end()
        else:
            temp = self.head.next
            prev = self.head
            for i  in range(1,pos-1):
                temp = temp.next
                prev = prev.next
            prev.next = temp.next
            #temp.next = None
                
        
node_1=Node(5)
node_2=Node(10)

cl=Cll()

cl.head=node_1
node_1.next=node_2

node_3=Node(15)
node_2.next=node_3

node_4=Node(20)
node_3.next=node_4

node_5=Node(25)
node_4.next=node_5

cl.tail=node_5
cl.tail.next=cl.head

cl.display()
print("\nAfter inserting at the beginning...")
cl.insert_beg(3)
cl.display()

print("\nAfter inserting at the end...")
cl.insert_end(30)
cl.display()

print("\nAfter inserting at pos 3...")
cl.insert_pos(2,6)
cl.display()

print("\nAfter deleting in the beginning...")
cl.delete_beg()
cl.display()

print("\nAfter deleting at the end...")
cl.delete_end()
cl.display()

print("\nAfter deleting at pos 3...")
cl.delete_pos(3)
cl.display()