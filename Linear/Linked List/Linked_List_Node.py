#Following is the blueprint of a Linked List node.
class Linked_List_Node:
  def __init__(self, data):  #Constructor
    self.data = data    #Data which is passed as input while object creation. Let's assume data to be any of these types-->(String, Integer, Float) 
    self.next = None    #Pointer To The Next Node If There Are More Than One Element Present In The Linked List. Initiated as None Always.
