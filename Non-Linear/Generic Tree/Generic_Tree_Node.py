#Following is a general node class of a Generic Tree.
#In Generic Tree, each node can have any number of child nodes. For that reason we use a List as one of the attributes of the node class.

class Generic_Tree_Node:
    def __init__(self, data):
        self.data = data
        self.children = []
 
