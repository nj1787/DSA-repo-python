#Use Generic_Tree_Node.py file for creating a Generic_Tree_Node object.
#The following is the implementation(taking input and printing) of the Generic Tree.

def take_input():
    print('Enter Root Data')
    root_data = int(input())
    if root_data == -1:                               #If -1 is entered initially None is returned and it is considered Empty Tree.
        return None
    root = Generic_Tree_Node(root_data)               #Creation of Root Node
    print('Enter Number of Children of ', root.data)  #Ask for the number of children of each root node.
    child_count = int(input())
    for i in range(child_count):
        child = take_input()                          #Recursive Call To Append or Connect All Children Node with their Parent Node. 
        root.children.append(child)
    return root

def print_tree_detailed(root):                        
    if root is None:                                  #Empty Tree Condition
        return
    print(root.data, end = ':')                       #Print Root Data. The Root changes after each recursive call ends.
    for child in root.children:
        print(child.data ,end = ',')                  #Prints Child of each Root Node.
    print()                                           #To Print output of each root node in a new line.
    for child in root.children:
        print_tree_detailed(child)                    #Recursive Call taking input as each child node of the current root node.


r = take_input()                                      #Root of the tree gets stored in r.
print()
print_tree_detailed(r)                                #Print the tree in a detailed manner as shown below in I/O.

-------------------------------------------------------------SAMPLE I/O-----------------------------------------------------------------------

#Input
Enter Root Data
16
Enter Number of Children of  16
5
Enter Root Data
18
Enter Number of Children of  18
0
Enter Root Data
13
Enter Number of Children of  13
3
Enter Root Data
31
Enter Number of Children of  31
0
Enter Root Data
47
Enter Number of Children of  47
0
Enter Root Data
63
Enter Number of Children of  63
0
Enter Root Data
25
Enter Number of Children of  25
0
Enter Root Data
12
Enter Number of Children of  12
2
Enter Root Data
15
Enter Number of Children of  15
0
Enter Root Data
14
Enter Number of Children of  14
0
Enter Root Data
24
Enter Number of Children of  24
0

#Output
16:18,13,25,12,24,
18:
13:31,47,63,
31:
47:
63:
25:
12:15,14,
15:
14:
24:
