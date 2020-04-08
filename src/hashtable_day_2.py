from linked_list_lecture import *

# '''
# Linked List hash table key/value pair
# '''

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity): 
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        index = self._hash_mod(key)
        node = self.storage[index]
        if node: #hash collision 
            print("hash collision detected")
            while node: # iterates through all non-Null keys of the nodes within the hash table location
                if node.key == key: #if the current node's key matches the new insertion key
                    node.value = value #update the value
                    break
                elif node.next == None: #if the current node's next is None we are at the tail
                    node.next = Node(key,value) #create new Node at tail location
                    break
                else:
                    node = node.next  
        else:
            ll = LinkedList()
            ll.add_to_head(key,value)
            self.storage[index] = ll.head


        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key) 
        ll = LinkedList()
        ll.head = self.storage[index]
        ll.remove(key)
        self.storage[index] = ll.head
        # if node is not None:
        #     previous = node
        #     head = node
        #     while node:
        #         if node.key == key: #when match between current node and input key    
        #             print(node.key," matches ",key)
        #             print(previous.next,node.next)
        #             previous.next = node.next 
        #             self.storage[index] = head
        #             node = None
        #             break
        #         node = node.next #iteration: current node becomes the next node in the chain
        #         previous = node #iteration: current node becomes the node before the current node, 
        #             # this does not change what the current node is, it merely assigns the current node to the previous variable
     
    
        # else:
        #     print("Warning: Key does not exist")
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index] 
        while node:
            if node.key == key:
                return node.value
            node = node.next

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pairs = []
        for bucket in self.storage:
            if bucket != None:
                node = bucket
                while(node):
                    pairs.append((node.key,node.value))
                    if(node.next == None):
                        break
                    node = node.next
        self.capacity *= 2  # Number of buckets in the hash table
        self.storage = [None] * self.capacity
        for key,value in pairs:
            self.insert(key,value)
        return



if __name__ == "__main__":
    ht = HashTable(8)
    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    ht.insert("key-6", "val-6")
    ht.insert("key-7", "val-7")
    ht.insert("key-8", "val-8")
    ht.insert("key-9", "val-9")
    ht.resize()
    print(len(ht.storage))
    print(ht.retrieve("key-0"))
    # ht.retrieve("key-9")




    # ht = HashTable(8)
    # ht.insert("line_1", "Tiny hash table")
    # # print(ht.storage)
    # ht.insert("line_2", "Filled beyond capacity")
    # # # print(ht.storage)
    # ht.insert("line_3", "Linked list saves the day!")
    # # # print(ht.storage)
    # # # print(len(ht.storage))

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    ## Test remove
    # ht.remove("line_1")
    # print(ht.retrieve("line_1"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
