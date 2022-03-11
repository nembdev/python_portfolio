"""
use size + node at index to find the mid point of the list
use the midpoint to split the list
use a new linked list to hold the merge
loop while head is not None
append to merged

"""




class Node:
    """
    an object for storing a single linked list node
    stores any type of data
    """

    # holds the data
    data = None
    # reference to the next next node
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

# node at index
# size
class LinkedList:
    """single linked list"""

    # head = None

    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        [Head: 411]-> [343]-> [23]-> [Tail: 1]
        """
        # will hold our query
        nodes = []
        # set to first position
        current = self.head
        # while not none
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)  # print head
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)  # print tail
            else:
                nodes.append("[%s]" % current.data)  # print a middle value
            current = current.next_node
        return "-> ".join(nodes)  # combine into a string

    def is_empty(self):
        """checks if empty"""
        return self.head == None

    # convience for size, instead of a loop
    # o(n), linear, until we hit the tail node
    # count = tail = size
    def size(self):
        """
        returns number of nodes in the list
        """
        # sets initial value
        current = self.head
        count = 0

        while current != None:
            # iterator
            count += 1
            # iterates through the linked list
            # stops when
            current = current.next_node

        return count

    def add(self, data):
        """
        prepend/head first

        """
        # new node holds the passed in data
        new_node = Node(data)
        # sets the old head as next node
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        searches the ll for the first node holding a specific value
        returns the node
        """
        current = self.head
        # start search
        while current != None:
            if current.data == key:
                return current
            else:
                current = current.next_node  # move forward
        return None

    # insert - constant time operation
    # search - linear
    # overall - linear
    def insert(self, data, index):
        # want to add to the start?
        if index == 0:
            self.add(data)

        if index > 0:
            # holds data to be inserted
            new_node = Node(data)
            # how many steps to take
            position = index
            # where we are currently
            current = self.head
            # search by decreasing index until 1 before we're at the pos
            while position > 1:
                current = current.next_node

                # search by decreasing index until 1 before we're at the po
                position -= 1
            # holds node right before insert pos
            prev = current
            # store its link
            next = current.next_node

            # insert our new node
            prev.next_node = new_node
            # link our new node to the previous next node
            new_node.next_node = next
        pass

    # worst - linear
    # remove by key
    # if head, remove head
    # if found swap
    # if not found, store prev and move on
    def remove(self, key):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
            return current

    def remove_by_index(self):
        pass

    def read_at_index(self):
        pass

    # recieves midpoint
    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            # start at the top
            current = self.head
            # num movements
            position = 0

        # iterates
        while position < index:
            current = current.next_node
            position += 1


def merge_sort(linked_list):
    """
    divides until single node sublists
    merge sublists until sorted
    returns sorted linked list

    make a second linked list, right
    get midpoint of linked list
        node_at_index()

    left = upto mid
    right = second linked list, head

    sort
        3rd linked list
        iterate i
    """
    # empty or single
    if linked_list.size() <= 1:
        return linked_list
    # No nodes
    elif linked_list.head is None:
        return linked_list

    left, right = split(linked_list)
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def split(linked_list):
    # check for single node, empty, no head
    if linked_list == None or linked_list.head is None:
        # return entire thing
        left = linked_list
        right = None  # save space
        return left, right
    else:
        # size = linked_list.size()
        mid = linked_list.size() // 2


def merge_sort(linked_list):

    # check for base case
    # is it empty or None
    if linked_list.head == None or linked_list.size() <= 1:
        return linked_list

    left, right = split(linked_list)


def node_at_index(self, index):
    if index == 0:
        return self.head
    else:
        current = self.head
        position = 0

    while position < index:
        current = current.next_node
        position += 1
    return current


def split(linked_list):

    # base case
    if linked_list.head == None or linked_list == None:
        left = linked_list
        right = None

        return left, right
    else:
        size = linked_list.size()
        mid = size // 2

        # get the mid node
        # THIS IS THE LINKED LIST
        mid_node = linked_list.node_at_index(mid - 1)

        # assign full list
        left = linked_list

        # new list
        right = LinkedList()
        # set right to mid to end
        right.head = mid_node.next

        # cut the link
        mid_node.next_node = None

    return left, right


def merge(left, right):

    # new list
    merged = LinkedList()

    # fake head
    merged.add(0)

    # reference to head
    current = merged.head

    #
    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        # left is none or right is none

        # end of left
        if left_head is None:
            # append start of right
            current.next_node = right_head
            # move right forward
            right_head = right_head.next_node
        elif right_head is None:
            # append start of left
            current.next_node = left_head
            # move left forward
            left_head = left_head.next_node
        else:
            # get the data for l and r
            # sort
            l_data = left_head.data
            r_data = right_head.data

            if l_data < r_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        # move merged forward
        current = current.next_node

    # remove fake
    merged.head = merged.head.next_node

    return merged
