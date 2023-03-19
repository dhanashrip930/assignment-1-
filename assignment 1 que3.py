#Merge a linked list into another linked list at alternate positions

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Define Linked List class to represent the linked list
class LinkedList:
    def __init__(self):
        self.head = None
        
    # add a node to the end of the linked list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    # print the linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
        print()

    # merge two linked lists at alternate positions
    def merge_alternate(self, list2):
        curr1 = self.head
        curr2 = list2.head
        while(curr1 is not None and curr2 is not None):
            next1 = curr1.next
            next2 = curr2.next
            curr1.next = curr2
            curr2.next = next1
            curr1 = next1
            curr2 = next2
        list2.head = curr2
        
# test the program with a sample input
llist1 = LinkedList()
llist2 = LinkedList()
llist1.append(1)
llist1.append(2)
llist1.append(3)
llist1.append(4)
llist1.append(5)
llist2.append(6)
llist2.append(7)
llist2.append(8)
llist2.append(9)
llist2.append(10)
llist1.print_list()
llist2.print_list()
llist1.merge_alternate(llist2)
llist1.print_list()
