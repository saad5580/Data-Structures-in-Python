
# pylint: disable=protected-access

# Imports
from copy import deepcopy


class BST:

    def _turn_right(self, parent):
        """
        -------------------------------------------------------
        Turns the parent node to its right around its left child.
        Updates the heights of the turned nodes.
        Use: parent = self._turn_right(parent)
        -------------------------------------------------------
        Parameters:
            parent - the pivot node to rotate around (_BST_Node)
        Returns​‌​​​‌​‌:
            updated - the node that replaces the parent node (_BST_Node)
        -------------------------------------------------------
        """
        y = parent._right
        T2 = y._left
        y._left = parent
        parent._right = T2
        parent._height = 1 + \
            max(self._max_height_aux(parent._left),
                self._max_height_aux(parent._right))
        y._height = 1 + max(self._max_height_aux(y._left),
                            self._max_height_aux(y._right))

        return

    def max_height(self):
        """
        ---------------------------------------------------------
        Returns the maximum height of a bst.
        Use: height = bst.max_height()
        ---------------------------------------------------------
        Returns​‌​​​‌​‌:
            height - the length of the longest path from the
                root node to the base of a tree (int)
        ---------------------------------------------------------
        """
        height = self._max_height_aux(self._root)
        return height

    def _max_height_aux(self, node):
        """
        ---------------------------------------------------------
        Private auxiliary method for 'max_height'.
        Returns the maximum height of node.
        Use: height = self._max_height_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - a BST node (_BST_Node)
        Returns​‌​​​‌​‌:
            height - the maximum height of node (int)
        ---------------------------------------------------------
        """
        if node is None:
            return 0

        leftAns = self._max_height_aux(node._left)
        rightAns = self._max_height_aux(node._right)

        return max(leftAns, rightAns) + 1

    def max_path(self):
        """
        ---------------------------------------------------------
        Returns a list of nodes in the longest path of a bst.
        Use: path = bst.max_path()
        ---------------------------------------------------------
        Returns​‌​​​‌​‌:
            path - a list of nodes of the longest path from the
                root node to the base of a tree (list of _BST_Node)
        ---------------------------------------------------------
        """
        path = self._max_path_aux(self._root)  # your parameters here
        return path

    def _max_path_aux(self, node):  # your parameters here
        """
        ---------------------------------------------------------
        Private auxiliary method for 'max_path'.
        Returns a list of the nodes in the longest path from node to the
        base of a tree.
        Use: path = self._max_height_aux( # your doc here )
        ---------------------------------------------------------
        Parameters:
            # your doc here
        Returns​‌​​​‌​‌:
            path - a list of the nodes in the longest path from node
                to the base of a tree (list of _BST_Node)
        ---------------------------------------------------------
        """
        if node is None:
            return []

        right = self._max_path_aux(node._right)

        left = self._max_path_aux(node._left)

        if len(left) > len(right):
            left.append(node)
        else:
            right.append(node)

        if len(left) > len(right):
            return left

        return right

    def flip(self):
        """
        ---------------------------------------------------------
        Changes the current BST into a flipped image of itself. All nodes
        are swapped with nodes on the other side of a tree. Nodes may take
        the place of an empty spot. The resulting tree is a flipped image
        of the original tree. (Note that the flipped tree is not a BST.)
        Use: bst.flip()
        ---------------------------------------------------------
        Returns​‌​​​‌​‌:
            None
        ---------------------------------------------------------
        """
        self._flip_aux(self._root)
        return

    def _flip_aux(self, node):
        """
        ---------------------------------------------------------
        Changes the current subtree into a flipped image of itself. All nodes
        are swapped with nodes on the other side of a tree. Nodes may take
        the place of an empty spot. The resulting subtree is a flipped image
        of the original subtree.
        Use: self._flip_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - a binary tree node (_BST_Node)
        Returns​‌​​​‌​‌:
            None
        ---------------------------------------------------------
        """
        if node is None:
            return
        else:
            temp = node

            self._flip_aux(node._left)
            self._flip_aux(node._right)

            temp = node._left
            node._left = node._right
            node._right = temp

        return


# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns​‌​​​‌​‌:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into bst. Values may appear
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into bst (?)
        Returns​‌​​​‌​‌:
            inserted - True if value is inserted into bst,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into node.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns​‌​​​‌​‌:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into node,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in bst. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns​‌​​​‌​‌:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns​‌​​​‌​‌:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._inorder_aux(self._root, a)
        return a

    def _inorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses node subtree in inorder. a contains the contents of
        node and its children in inorder.
        Private recursive operation called only by inorder.
        Use: self._inorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - target list of data (list of ?)
        Returns​‌​​​‌​‌:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            self._inorder_aux(node._left, a)
            a.append(deepcopy(node._value))
            self._inorder_aux(node._right, a)
        return

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns​‌​​​‌​‌:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._preorder_aux(self._root, a)
        return a

    def _preorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses node subtree in preorder. a contains the contents of
        node and its children in preorder.
        Private recursive operation called only by preorder.
        Use: self._preorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - target of data (list of ?)
        Returns​‌​​​‌​‌:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            a.append(deepcopy(node._value))
            self._preorder_aux(node._left, a)
            self._preorder_aux(node._right, a)
        return

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns​‌​​​‌​‌:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a is_valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns​‌​​​‌​‌:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        valid = self._is_valid_aux(self._root, None, None)
        return valid

    def _is_valid_aux(self, node, min_node, max_node):
        """
        ---------------------------------------------------------
        Private recursive method to determine the BST validity of node,
        used only by is_valid.
        Use: valid = self._is_valid_aux(node, min_node, max_node)
        ---------------------------------------------------------
        Parameters:
            node - a binary tree node (_BST_Node)
            min_node - the node with the minimum value for the current tree (_BST_Node)
            max_node - the node with the maximum value for the current tree (_BST_Node)
        Returns​‌​​​‌​‌:
            valid - True if node is root of a valid BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if node is None:
            valid = True
        elif min_node is not None and node._value <= min_node._value:
            # print("BST left value violation at value: {}".format(node._value))
            valid = False
        elif max_node is not None and node._value >= max_node._value:
            # print("BST right value violation at value: {}".format(node._value))
            valid = False
        elif node._height != max(self._node_height(node._left), self._node_height(node._right)) + 1:
            # print("BST height violation at value: {}".format(node._value))
            valid = False
        else:
            # node becomes max node of left tree, min node of right tree
            valid = self._is_valid_aux(node._left, min_node, node) \
                and self._is_valid_aux(node._right, node, max_node)
        return valid


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns​‌​​​‌​‌:
            A _BST_Node object (_BST_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        self._count = 0

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node. _height is 1 plus
        the maximum of the node's (up to) two child heights.
        Use: node._update_height()
        -------------------------------------------------------
        Returns​‌​​​‌​‌:
            None
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return f"h: {self._height}, v: {self._value}"
