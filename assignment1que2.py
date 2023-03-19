#Reverse a linked list in groups of given size
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Define Linked List class to represent the linked list
class LinkedList:
    def __init__(self):
        self.head = None
        
    def reverse_group(self, head, k):
        prev = None
        curr = head
        nxt = None
        count = 0

        # reverse first k nodes of the linked list
        while (curr is not None and count < k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1

        # recursive call to reverse the remaining part of the linked list
        if nxt is not None:
            head.next = self.reverse_group(nxt, k)

        # prev is new head of the input list
        return prev

    # add a node to the beginning of the linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # print the linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
        print()

# test the program with a sample input
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.print_list()
llist.head = llist.reverse_group(llist.head, 3)
llist.print_list()

