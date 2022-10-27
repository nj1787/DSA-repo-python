#The follwing code implements a Binary Tree in preorder manner.

#Preorder traversal happens in the order ROOT-->LEFT-->RIGHT.

#It consists for two functions : take_input() and print_tree().

#Takes input of Binary Tree Nodes in Preorder Format.Returns the root of the Binary Tree.
def take_input():
    root_data = int(input())      #Let's Assume Data to be of the types (String, Integer, Float)
    if root_data == -1:           #Condition To check whether the entire Binary Tree is empty or if only one of the left subtree or right subtree is empty.
        return None
    root = Binary_Tree(root_data) #Parametrized Constructor Call.Use the BT_Node.py file for the Binary Tree Class.
    left_input = take_input()     #Recursive call for taking inputs for left subtree. Stores value None if root_data has value -1.
    right_input = take_input()    #Recursive call for taking inputs for right subtree. Stores value None if root_data has value -1.
    root.left = left_input        #Connecting root of left subtree with the left of the root of Binary Tree. 
    root.right = right_input      #Connecting root of right subtree with the right of the root of Binary Tree.
    return root

#Prints the Binary Tree in Preorder Format. Takes in root of the Binary Tree as formal argument(s).
def print_tree(root):
    if root is None:              #Condition To check whether the entire Binary Tree is empty or if only one of the left subtree or right subtree is empty.
        return
    print(root.data, end = ':')   #Prints Root of the Binary Tree and further prints roots of left subtree and right subtree after the recursive calls.
    if root.left is not None:
        print('L', root.left.data, end = ',') #Prints Left Node Data of either the main root of the Binary Tree or roots present within Left Subtree.Blank Outpput if root.left is None.
    if root.right is not None:
        print('R', root.right.data, end = '') #Prints Right Node Data of either the main root of the Binary Tree or roots present within Right Subtree.Blank Output if root.right is None.
    print()
    print_tree(root.left)         #Recursive Call To Print Left Subtree with root of left subtree as parameter (Tail Recursion)
    print_tree(root.right)        #Recursive Call To Print Right Subtree with root of right subtree as parameter (Tail Recursion)

#Main Body
r = take_input() #Returns root of the Binary Tree
print()
print_tree(r) #Takes in root of the tree as actual argument(s).

-----------------------------------------------------------------Sample I/O---------------------------------------------------------------------------------------
#Input
18
15
41
-1
-1
-1
24
33
-1
-1
26
-1
-1

#Output                      
18:L 15,R 24
15:L 41,
41:
24:L 33,R 26
33:
26:
