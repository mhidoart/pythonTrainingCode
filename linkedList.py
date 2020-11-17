class Node:

    def __init__(self,data=None,next=None):
        self.data =data
        self.next=next


    def print_node(self):
        print(self.data)

    def __repr__(self):
        if(self.data):
            if(self.next):
                return str(str(self.data)+" => ")
            else:
                return str(self.data)
        else:
            return ""
class LinkedList:
    def __init__(self):
        self.head=None
    def append_node(self,data):
        if not self.head:
            self.head =Node(data)
        else:
            current =self.head
            while current.next:
                current =current.next
            current.next = Node(data)
    def __repr__(self):
        current=self.head
        myLinkedList =""
        while(current):
            myLinkedList += str(current)
            current =current.next
        return myLinkedList
    def search(self,target):
        current = self.head
        while(current):
            print(current.data," ", target)
            if(str(current.data) == str(target)):
                print("Found it !!")
                return True
            else:
                current = current.next
        print("Not found !!")
        return False


ll = LinkedList()
ll.append_node(Node("mehdi"))
ll.append_node(Node("Assabbane"))
ll.append_node(Node("23"))
ll.append_node(Node("ENSIIE"))
ll.append_node(Node("PARCOURS LIBRE"))
print(ll)
ll.search("mehdi")
