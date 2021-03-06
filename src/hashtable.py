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
        # if len(self.storage) >= self.capacity:
        #     self.resize()
        index = self._hash_mod(key)
        node = self.storage[index]
        if node: #hash collision 
            while node.next: # iterates through all non-Null keys of the nodes within the hash table location
                  if node == None:
                      continue
            
            != key:
                node.next = Node(key,value)
                # node.key = key #overwriting the key (primitive)
            node.value = value

        else:
            self.storage[index] = Node(key,value) 


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
        if self.storage[index] and self.storage[index].key == key:
            self.storage[index] = None
        else:
            print(key," was not found")
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] and self.storage[index].key == key:
            return self.storage[index].value

        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        return self.capacity * 2



if __name__ == "__main__":
    ht = HashTable(2)
    ht.insert("line_1", "Tiny hash table")
    # print(ht.storage)
    ht.insert("line_2", "Filled beyond capacity")
    # # print(ht.storage)
    ht.insert("line_3", "Linked list saves the day!")
    # # print(ht.storage)
    # # print(len(ht.storage))

    print("")

    # # Test storing beyond capacity
    print(ht.retrieve("line_1"))
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
