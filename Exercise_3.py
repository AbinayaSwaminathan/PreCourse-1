#Time Complexity : O(N)
#Space Complexity : O(N)
#Any problem you faced while coding this : No
class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == key:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Key not found in the list")
        return current

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == key:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Key not found in the list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
