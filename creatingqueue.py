def enqueue_element():
    if len(que)==n:
        print("queue is full")
    else:
        n1=input("enter the element in the queue")
        que.append(n1)
        print(que)

def dequeue_element():
    if not que:
        print("queue is emplty add the element")
    else:
        n1=que.pop(0)
        print(n1,"removed")
        print(que)

que=[]
n=int(input("enter the size"))
while True:
    print(" select the operation 1.enqueue 2.dequeue 3.exit")
    choice=int(input())
    if choice==1:
        enqueue_element()
    elif choice==2:
        dequeue_element()
    elif choice==3:
        break
    else:
        print("the correct operation!")