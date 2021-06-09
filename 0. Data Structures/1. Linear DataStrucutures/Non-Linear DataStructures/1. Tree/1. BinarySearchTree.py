# Tree is a type of non-linear data structure in which data is connected in a hierarchy
# Root node is the top node, which is the only node in level 0 and con't have any parent nodes.

# Binary search tree is a tree in which each node atmost 2 childs.

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

# If new node comes, first compare it with root Node
# If the value is less than the current node, then move it left. 
# and if the value is greater than current node, then move to right.
# This procedure repeat for aevery subtree until find a leaf node which having not child nodes.
# If no nodes are there in a tree, the new node can be the root node of the tree
def insert( root, value):
    if root is None:
        root = Node(value)
        return root
    if value < root.value:
        root.left = insert( root.left, value)
    else:
        root.right = insert( root.right, value)

    return root

#Traversal in BST is means, we print the values of each node in a purticular sequence.

# In the Pre-Order Traversal, we print the value of root in first place.
# Then print the left child value and then right child value.
# This sequence of root->left->right should follow in all the sub-trees.
def preOrder(root):
    if root:
        print(root.value)
        preOrder(root.left)
        preOrder(root.right)

# In In-Order traversal, the root value will print at center
# Left chile value printed first, then the root value then the right child value.
# This sequence has to be follow all the subtree in the binary tree
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.value)
        inOrder(root.right)

# In post-Order Traversal, the value of the root node printed at the end. 
# First print the left child value and then right child value.
# Finally the root value printed at last.
# This sequence have to be follow in all the subtree of the binary tree.
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.value)


# The left most node will be always the minimum valued node in a Binary Search Tree.
def getMinimumValueNode(root):
    if root:
        while root.left is not None:
            root = root.left
        return root

# There is three possibility of deleting a node from BST.
# 1. Deleting a leaf node -> we can directly delete the leaf node as because it don't have any child.
# 2. Deleting a node with one child -> When we delete the node, the child can take its position in BST.
# 3. Deleting node with both childs -> We have to find the node which can take its position.
# Move right to the node which wnt to delete and find the minimum valued node of the subtree, 
# This is the only node that can take the position of the node which deleting.
def deleteNode( root, value):
    if root is None:
        return root
    
    if value < root.value:
        root.left = deleteNode( root.left, value)
    elif value > root.value:
        root.right = deleteNode( root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            temp = getMinimumValueNode(root.right)
            root.value = temp.value
            root.right = deleteNode(root.right, temp.value)

    return root


#Input Sample BST
#             50
#
#     10              80
#
# 2       15      60      90
root = Node(50)
insert( root, 10)
insert( root, 2)
insert( root, 80)
insert( root, 15)
insert( root, 60)
insert( root, 90)

print("Pre-order traversal!")
preOrder(root)

print("In-order traversal!")
inOrder(root)

print("Post-order traversal!")
postOrder(root)

print("Minimum Valued Node is")
print(getMinimumValueNode(root).value)

print("Delete Node 50 from BST!")
root_50 = deleteNode( root, 50)

print("Post-order traversal!")
postOrder(root)