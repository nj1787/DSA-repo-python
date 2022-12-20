#For Linked List Node, Print Linked List and Taking Input of Linked List Please use the respective files in the Linked List Folder.

#Here I have just implemented two generic functions which inserts a Linked List Node at any given position passed as a parameter.

#Recursive Implementation
def insert_node(head, index, data):
    
    if index < 0:                                             #Used to handle any invalid(less than 0) index passed as parameter. 
        return head                                           #Return the original linked list as it is
    
    if index == 0:                      #Actual Base Case - At each recursive call, decremented index value is passed and last value it can reach is zero.
        new_node = Linked_List_Node(data)                          #First Create the new node with the passed data.
        new_node.next = head                                  #The next of new node will contain the address currently present in the head.
        return new_node                                       #Returns the new node as temporary head.
    
    if head is None:                                          #This is used to handle if index is out of bounds(Index Greater than Actual Length)
        return head                                           #Return the original linked list as it is
    
    small_output = insert_node(head.next, index - 1, data)    #Recursive Call - Small output refers to the temporary head returned by the function.

    head.next = small_output                                  #The Original head of the linked list will now have address of this temporary head.

    return head                                               #Return Actual Head.

#Main
h = take_input()
print()
print_list(h)
print()
new_h = insert_node(h, 0, 31)                                #This function returns a new head after modifications done above.
print_list(new_h)

-------------------------------------------------------------Sample I/O-------------------------------------------------------------------------------

10 20 30 40 50 60 70 -1                               #Input

10-->20-->30-->40-->50-->60-->70-->None               #Output

31-->10-->20-->30-->40-->50-->60-->70-->None          #Output

10 20 30 40 50 60 70 -1                               #Input

10-->20-->30-->40-->50-->60-->70-->None               #Output

10-->20-->30-->40-->50-->60-->70-->31-->None          #Output
