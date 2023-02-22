# Reverse the linked list

class Node():
    def __init__(self, val):
        self.value = val
        self.next = None


class Reverse_Linked_List():
    def reverse_llist(self, head: Node):
        hare = head
        temp = []
        while hare:
            temp.append(hare.value)
            if hare.next:
                hare = hare.next
            else:
                break
        print(temp)
        temp = reversed(temp)
        for i in temp:
            print(i)


r_llist = Reverse_Linked_List()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

r_llist.reverse_llist(node1)
