'''LinkedListConstruction.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0121
print(" ")

# This is an input class. Do not edit.


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Feel free to add new properties and methods to the class.


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    '''
    This method will set the head of the linked list

    If the LL does NOT have a head node
        meaning: the linked list is empty
        then, set the head to equal the node
        then, set the tail to equal the node
        return
    
    If the LL does have a head node,
        meaning, the linked list exists
        then, call the insertBefore method 
            pass the current head node as the current node
            pass the new head node as the nodeToInsert
    '''
    # Time: O(1) | # Space: O(1)

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)

    '''
    This method will set the tail of the linked list

    If the LL does NOT have a tail node
        meaning: the linked list is empty
        then, set the head to equal the node
        then, set the tail to equal the node
        return
    
    If the LL does have a tail node,
        meaning, the linked list exists
        then, call the insertAfter method 
            pass the current tail node as the current node
            pass the new tail node as the nodeToInsert
    '''
    # Time: O(1) | # Space: O(1)

    def setTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertAfter(self.tail, node)

    '''
    This method will insert a node BEFORE a given node.
    
    If the linked list only has one node, and the nodeToInsert is that same node
        Then, we want to do nothing.
        - return

    In the case of the nodeToInsert already existing in the LL,
        then, we need to remove it prior to inserting it in any location
            including the same location that it is already in
            call the remove method on the nodeToInsert

    To insert a node in a linked list
        update the nodeToInsert pointers to point to the surrounding nodes
            update the nodeToInsert previous pointer to equal the current node's previous pointer
                this will allow the nodeToInsert to point to the node "before" it
            
            update the nodeToInsert next pointer to point to the current node
                this will allow the nodeToInsert to point to the node "after" it
        
        update the surrounding nodes pointers to point to the nodeToInsert
            if the current node previous pointer is None
                Then, the current node is the head of the LL
                And, since we need to insert a node BEFORE the head of the LL,
                    update the head of the LL to be the nodeToInsert

            if the current node previous pointer is NOT None
                then, the current node is NOT the head of the LL
                so, update the current node's previous node's next pointer to point to the nodeToInsert
                    this is connecting the old previous node of the current node to be the previous node of the nodeToInsert
            
            to insert the nodeToInsert before the current node.
                update the current node's previous pointer to point to the nodeToInsert
    '''
    # Time: O(1) | # Space: O(1)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return None
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert

        node.prev = nodeToInsert

    '''
    This method will insert a node AFTER a given node.
    
    If the linked list only has one node, and the nodeToInsert is that same node
        Then, we want to do nothing.
        - return

    In the case of the nodeToInsert already existing in the LL,
        then, we need to remove it prior to inserting it in any location
            including the same location that it is already in

    To insert a node in a linked list
        update the nodeToInsert pointers to point to the surrounding nodes
            update the nodeToInsert previous pointer to equal the current node
                this will allow the nodeToInsert to point to the node "before" it
            
            update the nodeToInsert next pointer to point to the current node's next pointer
                this will allow the nodeToInsert to point to the node "after" it
        
        update the surrounding nodes pointers to point to the nodeToInsert
            if the current node next pointer is None
                Then, the current node is the tail of the LL
                And, since we need to insert a node AFTER the tail of the LL,
                    update the tail of the LL to be the nodeToInsert

            if the current node next pointer is NOT None
                then, the current node is NOT the tail of the LL
                so, update the current node's next node's previous pointer to point to the nodeToInsert
                    this is connecting the old next node of the current node to be the next node of the nodeToInsert
            
            to insert the nodeToInsert AFTER the current node.
                update the current node's next pointer to point to the nodeToInsert
    '''
    # Time: O(1) | # Space: O(1)

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return None
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert

        node.next = nodeToInsert

    '''
    This method will insert a node at a given postion
    
    If the positon to insert the given node is postion 1
        meaning: we need to set a new head node
        then, call the setHead method
        return
    
    To keep track of what postion we are at in the LL,
        create a variable to store the current postion

    Start at the head
    Perform a while loop
        That will iterate while the current node's value is NOT none.
            meaning: so long as we are not at the end of the linked list.
            Also, the base case of the head node == none is taken care of here.
        And will iterate until the current postion == insert postion
            meaning: we have found the node we are searching for
        Else,
            continue to iterate to the next node and increment the current postion.
                meaning, continue iterating until one of the while loop conditions are false.


    If and when we break out of the while loop, then either
        node == None:
            meaning: we have traversed the full length of the LL
            if, we have travesed the full length of the LL and our current_position != given_positon
            then, our given_positon is greater than the length of the LL 
            and we can just insert the node at the tail
                - call the setTail method
        
        current_position == given_positon
            meaning: we found where we want to insert the node
            then, call the insertBefore method on the current node
    '''
    # Time: O(p) | # Space: O(1)

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return None

        node = self.head
        current_position = 1
        while node is not None and current_position != position:
            node = node.next
            current_position += 1

        if node is None:
            self.setTail(nodeToInsert)
            return None

        self.insertBefore(node, nodeToInsert)

    '''
    Given a LL and a value 
        Search the linked list for the value and remove each occurrence
    
    To serach through the linked list, start at the LL's head node
    Perform a while loop
        That will iterate while the current node's value is NOT none.
            meaning: so long as we are not at the end of the linked list.
            Also, the base case of the head node == none is taken care of here.
        
        To prevent losing the current node during the removal process of that node
            We need to store the current node in a temp variable
            Then, iterate the current node.
        
        determine if this node's value is equal to the given value
            If so, we have found a node that we want to remove
                Call the remove method on this node
    '''
    # Time: O(n) | # Space: O(1)

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            node_to_remove = node
            node = node.next
            if node_to_remove.value == value:
                self.remove(node_to_remove)

    '''
    Given a LL and node to remove
        We want to remove this node while preserving the linked list
            to do so, preserve the surrounding nodes

    Check if the node to remove is the head
        If so, we want to update the head to be the following node.
        This will take care of the LL's .head attribute

    Check if the node to remove is the tail
        If so, we want to update the tail to be the previous node.
        This will take care of the LL's .tail attribute
    
    We want to update all pointers impacted by the removal of this node.
        update the surrounding node's pointers
        update the current node's pointers
    '''
    # Time: O(1) | # Space: O(1)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.remove_pointers(node)

    '''
    The action of removing a node from a LL 
        update the surrounding nodes
        update the node's pointers
    
    If we do not connect/point the previous node's next pointer to the next "node" in the linked list
        Then, the linked list would be broken when traversing forwards
        - IF the previous node of the node to remove exist,
            - THEN, update the previous node's next pointer to equal the next pointer of the node to remove.
    
    If we do not connect/point the next node's previous pointer to the previous "node" in the linked list.
        Then, the linked list would be broken when traversing backwards
        - IF the next node of the node to remove exist,
            - THEN, update the next node's pervious pointer to equal the previous pointer of the node to remove.
    
    Now, we do not need the node to remove's previous pointer any more, we can remove it.
        - update the node to remove's previous pointer to None
    
    Now, we do not need the node to remove's next pointer any more, we can remove it.
        - update the node to remove's next pointer to None
    '''
    # Time: O(1) | # Space: O(1)

    def remove_pointers(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    '''
    Traverse the linked list and check if a node has the same value as the given value.

    Start at the head or tail
    Perform a while loop
        That will iterate while the current node's value is NOT none.
            Meaning, so long as we are not at the end of the linked list.
            Also, the base case of the head node == none is taken care of here.
        And will iterate until the current node's value is equal to the given value.
            Meaning, we have found the node we are searching for
        Else,
            continue to iterate to the next node
                meaning, continue iterating until one of the while loop conditions are false.


    If and when we break out of the while loop, then node must be one of two things.
        Either we have found the node we are looking for.
            node.value == given value
            then, we want to return this node
        Or, we did not find the node we are looking for.
            node == None
            then, we want to return None
    '''
    # Time: O(n) | # Space: O(1)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        if node is not None:
            return node


# _recursion
# _iteration
print(" ")
