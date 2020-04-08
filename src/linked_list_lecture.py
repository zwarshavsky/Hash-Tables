class Node:
    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, key, value):
        self.head = Node(key, value, self.head)

    # def return_tail(self):
    #     node = self.head
    #     while node:
    #         node = node.next
    #         if not node.next:
    #             return node 
    
    def update(self,key,value):
        pass
        
    def remove(self, key):
        '''
        Find and remove the node with the given value
        '''
        if not self.head:
            print("Error: Value not found")
        elif self.head.key == key:
            # Remove head value
            self.head = self.head.next
        else:
            parent = self.head
            current = self.head.next
            while current:
                if current.key == key:
                    # Remove value
                    parent.next = current.next
                    return
                current = current.next
            # print("Error: Value not found")

    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def print(self):
        current = self.head
        ll_str = ""
        while current:
            ll_str += f"{current.value}"
            current = current.next
            ll_str += " -> "
        ll_str += "None"
        # print(ll_str)


# ll = LinkedList()
# ll.print()
# ll.add_to_head(1)
# ll.add_to_head(2)
# ll.add_to_head(3)
# ll.print()
# ll.remove(2)
# ll.print()