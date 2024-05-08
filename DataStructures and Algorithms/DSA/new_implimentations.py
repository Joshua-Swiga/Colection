class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
   
    # Setters
    def set_value(self, val):

        self.value = val

        return self.value
   
    def set_next(self, value):
        self.next = value


    # Getters
    def get_value(self):
        return self.value
   
    def get_next(self):
        return self.next
   


    # def __repr__(self) -> str:
    #     return '<Node: %s>' %self.value


class LinkedList:


    def __init__(self):
        self.head = None
        self.counter = 0


    def insert(self, val):
        if val:
            new = Node(val)

            new.set_next(self.head)
            self.head = new


            self.counter += 1
   
    def __repr__(self) -> str:
        elements: list = []
        current = self.head
        while current:


            if current.get_value() == self.head.get_value():
                elements.append('[Head: %s]' %current.get_value())
            elif current.get_next() == None:
                elements.append('[Tail: %s]' %current.get_value())


            else:
                elements.append('[ %s ]' %current.get_value())


            current = current.get_next()


        return ' -> '.join(elements)
   


    def search(self, key):
        # Returns the value that is associated with the key, not the index
        # Runs in O(n)
        
        '''
        current = self.head # This sets current to the first value of the linked list
        while current: #This says that as long as current is not None
           

           # Comparing whether the current value is euqual to the key/target value
            if current.get_value() == key:
                return current.get_value()
           
            else:
                # If it is not, we set current to the next value in the array
                current = current.get_next()
           
        return None
        '''

        current = self.head

        while current is not None:
            if current.get_value() == key:
                return current.get_value()
            else:
                current = current.get_next()

        return None
            
    # Read on this comprehensively
    def remove(self, key):
        current = self.head
        previous = None # This has been set to none because there is no node that is before the current/head value
        found = False

        while current and not found: # This will evaluate based on whether current has a value and found is false
            if current.get_value() == key and current is self.head:
                found = True # Read on how this terminates the loop

                self.head = current.get_next()

            elif current.get_value() == key:
                found = True
                previous.set_next(current.get_next())
                '''
                since previous is keeping truck of the node before the curent, we need to update
                its memory reference to point to the one after the one we want to remove.
                
                '''

            else:
                previous = current
                current = current.get_next()

        return current

"""
Let's go through the notes and explanations for each part of the `remove` method:

1. **Using `current.get_value()`**: In a linked list, each node contains a value (or data) and a reference to the next node. To access the value of a node, we use the `get_value()` method. So, when comparing the value of the current node with the key, we use `current.get_value()` to retrieve the value of the current node.

2. **Updating the next reference of the previous node**: When we find the node with the key to remove (`current`), we need to update the next reference of the node that precedes it (`previous`). This is crucial because removing a node from a linked list involves changing the next reference of the node before the one being removed to skip over the removed node. We accomplish this by setting the next reference of `previous` to point to the node after `current`, effectively bypassing `current`.

3. **Decrementing the counter**: The `counter` attribute of the linked list keeps track of the number of elements in the list. When we successfully remove a node from the list, we decrease the counter by one to reflect the updated number of elements.

4. **Returning `True` if the key is found and removed**: The `found` variable is used to track whether the key has been found and removed from the list. If the key is found and removed (`found` is `True`), we return `True` to indicate that the removal was successful. Otherwise, if the key is not found in the list (`current` becomes `None`), we return `False` to indicate that the removal operation did not occur.

By following these steps and explanations, the `remove` method effectively removes a node with the specified key from the linked list and updates the list's state accordingly.


Certainly! In the `remove` method of the `LinkedList` class, the variable `previous` is used to keep track of the node that precedes the current node (`current`) as we iterate through the linked list. Let's break down its function:

1. **Initialization**: Initially, `previous` is set to `None` because there is no node before the head of the linked list.

2. **Loop Iteration**: During the iteration through the linked list to find the node with the specified key (`current`), `previous` keeps track of the node before `current`. This is essential because when we find the node to remove (`current`), we need to update the next reference of the node before it to bypass `current` after removal.

3. **Updating `previous`**: In each iteration of the loop, `previous` is updated to be equal to the current node (`current`). This ensures that `previous` always points to the node before the current one.

4. **Handling Special Cases**: `previous` is crucial for handling special cases, such as when the node to remove is the head of the linked list. In such cases, we update the head directly without referencing `previous`. However, for nodes in other positions, we need to update the next reference of the node before the one being removed, and `previous` facilitates this.

In summary, `previous` is a reference to the node that comes before the current node (`current`) as we traverse the linked list. It plays a crucial role in updating the structure of the linked list when removing a node.
"""


"""
Read on inserting an element at an index

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert(data)

        if index > 0:
            new = Node(data)

            possition = index
            current = self.head

            while possition > 1:
                pass
"""
       
l=LinkedList()
l.insert(42)
l.insert(345)
l.insert(352)
l.insert(6)
l.insert(2)


print(l)

search_alg = l.search(6)
print(search_alg)

l.remove(345)
print(l)