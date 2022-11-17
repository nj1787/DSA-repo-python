#Use the Linked_List_Node.py file for the Node class.

def take_input():
  input_list = [int(ele) for ele in input().split()]   #Take input in form of a Array/List
  head = None                                          
  tail = None                                             
  for ele in input_list:
      if ele == -1:                                    #If the input_list consists of only single -1, then loop ends and None is returned.(Empty List)
          break                                        #Else if -1 occurs at any position in the input_list, then loop ends. 
      new_node = Node(ele)                             #Creation of new linked list node
      if head is None:                                 #Empty Linked List.This line will run atleast once.
          head = new_node                              #The new node becomes the head and tail of the Linked List
          tail = new_node
      else:
          tail.next = new_node                         #Current tail's next stores address of new node
          tail = new_node                              #New node becomes the current tail.
  return head                                          

def print_list(head):
  while head is not None:                              #Codition to check end of Linked List or to check whether Linked List is empty i.e head is None.
    print(str(head.data) + '-->', end = '')          #Print node data
    head = head.next                                 #Move to next node and check whether current head is None or not.
  print('None')                                        #Will print only None if Linked List is empty or else will add None to the end of the Linked List.

'''Main Function'''
h = take_input()                                         
print()
print_list(h)

-------------------------------------------------------------SAMPLE I/O----------------------------------------------------------------------------------

I/P - 10 20 30 40 50 -1

O/P - 10-->20-->30-->40-->50-->None

I/P - 1 2 3 4 5 6 7 -1

O/P - 1-->2-->3-->4-->5-->6-->7-->None
