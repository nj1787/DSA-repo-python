#Use the BT_Node.py file to get the Binary_Tree class definition.
#Below is the implementation of two methods to take input as well as print the tree in LEVEL-ORDER-FORMAT
#Don't forget to import the inbuilt queue module.

def take_input():
    q = queue.Queue()                     #We use a queue data structure to maintain order of elements in which they appear in the tree.
    print('Enter Root Data')
    root_data = int(input())
    if root_data == -1:                   #Condition to check whether Binary Tree is Empty or Not
        return None                       #Empty Binary Tree 
    root = Binary_Tree(root_data)         #In-case above condition is FALSE, root node of tree is successfully created.
    q.put(root)                           #We add the node not the data of the node in the queue.
    while q.empty() is False:      
        curr_node = q.get()               #Access the current node i.e. left-most element of the queue.This also removes the element from the queue.
        print('Enter Left Child for ', curr_node.data)
        left_child_data = int(input())
        if left_child_data != -1:         #Condition to check whether left child is valid or not
            left_child = Binary_Tree(left_child_data)
            curr_node.left = left_child   #Connect the newly created node as the left child of the current node 
            q.put(left_child)             #Add the same to the queue so that it can be used as current node.
        print('Enter Right Child for ', curr_node.data)
        right_child_data = int(input())
        if right_child_data != -1:        #Condition to check whether right child is valid or not
            right_child = Binary_Tree(right_child_data)
            curr_node.right = right_child #Connect the newly created node as the right child of the current node.
            q.put(right_child)            #Add the same to the queue so that it can be used as current node.
    return root
    
def print_tree(root):
    q = queue.Queue()
    if root is None:
        return 
    q.put(root)
    while q.empty() is False:
        curr_node = q.get()
        print(curr_node.data, end = ':')
        if curr_node.left is not None:
            print('L', curr_node.left.data, end = ',')
            q.put(curr_node.left)
        if curr_node.right is not None:
            print('R', curr_node.right.data, end = '')
            q.put(curr_node.right)
        print()

#Main 
r = take_input()
print()
print_tree(r)

-----------------------------------------------------------SAMPLE I/O--------------------------------------------------------------------------
Enter Root Data
18
Enter Left Child for  18
16
Enter Right Child for  18
15
Enter Left Child for  16
-1
Enter Right Child for  16
-1
Enter Left Child for  15
14
Enter Right Child for  15
10
Enter Left Child for  14
12
Enter Right Child for  14
-1
Enter Left Child for  10
-1
Enter Right Child for  10
19
Enter Left Child for  12
-1
Enter Right Child for  12
-1
Enter Left Child for  19
-1
Enter Right Child for  19
-1

18:L 16,R 15
16:
15:L 14,R 10
14:L 12,
10:R 19
12:
19:
