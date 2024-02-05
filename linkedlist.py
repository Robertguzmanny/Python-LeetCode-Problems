# Robert J. Guzman CSI 33 Programing Assigment 2
from ListNode import ListNode


class SLList(object):
    # ------------------------------------------------------------
    def __init__(self):
        """create an SLList object
        post: an empty SLList has been created"""
        # self.lst=[]
        self.size = 0
        self.head = None

# ------------------------------------------------------------
    def insert_at_head(self, data):
        """insert a new ListNode with item data at the head
        #post: a new ListNode with item data has been inserted at the head of the list"""
        if (self.head == None):
            self.head = ListNode(data)
        elif (self.head != None):
            nextHead = ListNode(data, self.head)
            self.head = nextHead
        self.size += 1


# ------------------------------------------------------------

    def insert_after(self, noderef, data):
        """insert a new ListNode with item data after the node with reference noderef
        pre:  ReferenceNode is a reference to a ListNode in the SLList
        post:  a new ListNode with item data has been inserted after the node with reference noderef"""
        newNode = ListNode(data, None)
        ReferenceNode = noderef
        if (ReferenceNode.link == None):
            ReferenceNode.link = newNode
        elif (ReferenceNode.link != None):
            newNode.link = ReferenceNode.link
            ReferenceNode.link = newNode
        self.size += 1

    # ------------------------------------------------------------

    def delete_after(self, noderef):
        """delete the ListNode after the node with reference noderef and return its item
        pre:  noderef is a reference to a ListNode in the SLList
        post:  the node with reference noderef has been deleted and its item returned"""

        ReferenceNode = noderef
        if (ReferenceNode.link == None):
            pass
        elif (ReferenceNode.link != None):
            eliminateNode = ReferenceNode.link
            ReferenceNode.link = eliminateNode.link
            del eliminateNode
        self.size -= 1

      # ------------------------------------------------------------
    def search(self, data):
        """returns a reference to the first ListNode in self that has data for its item
        post:  returns a reference to the first ListNode with data,  returns None if data does not occur"""
        currNode = self.head
        while currNode != None:
            if currNode.item == data:
                return currNode
            currNode = currNode.link

        return 0
    # ------------------------------------------------------------

    def __len__(self):
        """returns the number of items in the SLList
        post:  returns the length of the SLList"""
        return self.size

    # ------------------------------------------------------------
    def print(self):
        """prints the items in the list
        post: The list has been printed to std out"""

        curr = self.head
        while curr != None:
            print(curr.item, end="  ")
            curr = curr.link

    # ------------------------------------------------------------
    def get_item(self, noderef):
        """returns the item at the noderef node
        pre:  noderef is a reference to a ListNode in the SLList
        post: returns the item at the noderef node"""

        return noderef.item
