#Linked_List

class ListNode:
    def __init__(self, data:int):
        self.data = data
        self.next = None
    def __iter__(self):
        current = self
        while current is not None:
            yield current # suspend and output current ListNode object
            current = current.next
            
def init_list(seq:list)->ListNode:
    head = None
    for i in seq:
        if head is None:
            head = ListNode(i)
            tail = head
        else:
            tail.next = ListNode(i)
            tail = tail.next
    return head




#########
def remove_duplicated(head:ListNode)->ListNode:
    
    ls=[]
    
    tail=head
    ls.append(head.data)
    while(tail.next):
        ls.append(tail.next.data)
        tail = tail.next
    
    print(ls)
    ls.sort()
    
    for i in range(len(ls)-1):
            if(ls[i]==ls[i+1]):
                ls[i]=""
                
    while "" in ls:
        ls.remove("")

    print(ls)
    
    head1=ListNode(ls[0])
    tail1=head1
    
    for i in range(1,len(ls)):
        tail1.next = ListNode(ls[i])
        tail1=tail1.next
        
#     print(head1.data)
#     tail1=head1
#     while(tail1.next):
#         print(tail1.data)
#         tail1 = tail1.next
    
    return head1
