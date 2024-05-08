class Node(object):
    def __init__(self, value: any):
        if value is not None:
            self.value = value
            self.next = None
        else:
            raise TypeError ("The value is void!")
    
    # Setters
    def set_value(self, val: any):
        if val:
            self.value = val

            return self.value
        else:
            print("Please provide a valid input!")

    def set_next(self, val: any):
        self.next = val
        return self.next
    
    # Getters
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next


class LinkedList(object):
    def __init__(self, head: any = None):
        self.head = head
        self.number_of_elements = 0

    # Inserting an element into the node...
    def insert (self, element):
        if element is not None:
            new_insert = Node(element)

            new_insert.set_next(self.head)
            self.head = new_insert
            self.number_of_elements += 1

    def delete(self, target: any):
        if target is not None:

            current = self.head
            previous = None

            # Checks whether we are dealing with the very first element
            if current.get_value() == target and current == self.head:
                self.head = current.get_next()
            
            # Checks for the rest of the elements
            while current is not None:
                if current.get_value() == target:
                    previous.set_next(current.get_next())

                else:
                    previous = current
                    current = current.get_next()
        else:
            print(f"Missing value: {target}")   


    def empty_list(self):
        if self.number_of_elements == 0:
            print("The list is Empty!")
        else:
            print(f"Number of objects: {self.number_of_elements}")


    def find(self, target: any):
        if target is not None:
            current = self.head

            if current.get_value() != None and current.get_value() == target:
                return current
            else:
                current = current.get_next()

            print(f"Void Value: {target}")
        
        else:
            raise TypeError ("Missing Possitional Argument")

    