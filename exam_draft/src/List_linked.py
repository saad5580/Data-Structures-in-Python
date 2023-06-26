
# pylint: disable=protected-access

from copy import deepcopy
from random import randint


class List:

    def append_list(self, source):
        """
        -------------------------------------------------------
        Private helper method to append the entire source List to the
        rear of the target List.
        Either the source List or the target List may be empty.
        The source list becomes empty.
        Use: target.append_list(source)
        -------------------------------------------------------
        Parameters:
            source - an linked list (List)
        Returns​‌​​​‌​‌:
            None
        -------------------------------------------------------
        """
        node = source._front

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += len(source)
        source._front = None
        source._rear = None
        return

    def split_sq(self):
        """
        -------------------------------------------------------
        Splits source into two parts. target1 contains the first half,
        target2 the second half. Current (source) List becomes empty.
        Uses Slow/Quick algorithm.
        Use: target1, target2 = source.split_sq()
        -------------------------------------------------------
        Returns​‌​​​‌​‌:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()

        # # Slow Quick algorithm
        quick = self._front
        slow = self._front
        while quick is not None:
            quick = quick._next
            if quick is not None:
                quick = quick._next
            if quick is not None:
                slow = slow._next

        temp = slow._next
        slow._next = None

        middle = self._count // 2 + self._count % 2

        target1._count = middle
        target1._front = self._front
        target1._rear = slow

        # Define target2
        target2._count = self._count - middle
        target2._front = temp

        if target2._count > 0:
            target2._rear = quick

        # Clean up source
        self._front = None
        self._rear = None
        self._count = 0

        return target1, target2

    def randomize(self):
        """
        -------------------------------------------------------
        Moves nodes from source to target in random order.
        All data is preserved, order is not. source is empty when
        finished.
        Use: target = source.randomize()
        -------------------------------------------------------
        Returns​‌​​​‌​‌:
            target - a new List with randomly ordered values from source (List)
        -------------------------------------------------------
        """
        target = List()

        return

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns​‌​​​‌​‌:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns​‌​​​‌​‌:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns​‌​​​‌​‌:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns​‌​​​‌​‌:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, self._front)

        if self._rear is None:
            # List is empty - update the rear of the List..
            self._rear = node
        # Update the front of the List.
        self._front = node
        self._count += 1
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns​‌​​​‌​‌:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def _move_front_to_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the front
        of the current List. Private helper method.
        Use: self._move_front_to_front(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns​‌​​​‌​‌:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        node._next = self._front
        self._front = node

        if self._rear is None:
            # Target list is empty
            self._rear = node
        self._count += 1
        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns​‌​​​‌​‌:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node

        node._next = None
        self._rear = node
        self._count += 1
        return

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns​‌​​​‌​‌:
            None
        -------------------------------------------------------
        """
        if pln is not prn:
            # Swap only if two nodes are not the same node

            if pln is None:
                # Make r the new front
                left = self._front
                self._front = prn._next
            else:
                left = pln._next
                pln._next = prn._next

            if prn is None:
                # Make l the new front
                right = self._front
                self._front = left
            else:
                right = prn._next
                prn._next = left

            # Swap next pointers
            # lst._next, r._next = r._next, lst._next
            temp = left._next
            left._next = right._next
            right._next = temp
            # Update the rear
            if right._next is None:
                self._rear = right
            elif left._next is None:
                self._rear = left
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns​‌​​​‌​‌:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns​‌​​​‌​‌:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
