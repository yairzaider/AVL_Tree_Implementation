#yair zaider - 207030149
#afik nitzan - 207412347



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
    """Constructor, you are allowed to add more fields. 
    
    @type key: int or None
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def __init__(self, key, value):
        if key!=None :                    ## creating a real Node
            self.key = key
            self.value = value
            self.left = AVLNode(None,None)  
            self.right = AVLNode(None,None)
            self.parent = None
            self.height = -1
            self.size = 0
            self.bfs =0
        else:                              ## creating  a virtual Node
            self.key = None
            self.value = None
            self.left = None
            self.right = None
            self.parent = None
            self.height = -1
            self.size = 0
            self.bfs =0

    """ getters & setters for all fields"""

    def get_key(self):
        return self.key
    
    def set_key(self,new_key):
        self.key= new_key
    
    def get_value(self):
        return self.value 
    
    def set_value(self, new_value):
        self.value= new_value

    def get_left(self):
        return self.left

    def set_left(self,left_node):
        self.left= left_node

    def get_right(self):
        return self.right
    
    def set_right(self, right_node):
        self.right= right_node
    
    def get_parent(self):
        return self.parent
    
    def set_parent(self, parent_node):
        self.parent= parent_node

    def get_height(self):
        return self.height
    
    def set_height(self, new_height):
        self.height= new_height
    
    def get_size(self):
        return self.size
    
    def set_size(self, new_size):
        self.size= new_size
    
    def get_bfs(self):
        return self.bfs

    def set_bfs(self,new_bfs):
        self.bfs = new_bfs

 
    """returns whether self is not a virtual node 
       Complexity : O(1)
    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """ 

    def is_real_node(self):
        
        if self.key!=None:             # if the key of the node is None so it is a virtual Node	
            return True
        else:
            return False
    
    """preforms a right rotation on given node 
       Complexity : O(1)
    @type avl_node: AVLNode
    @param avl_node: node to be rotated
    
    """

    def right_rotation(avl_node):    # the function performs a right rotation on 3 nodes as demonstrated in class 
        B = avl_node
        A =avl_node.get_left()
        B.set_left(A.get_right())
        B.get_left().set_parent(B)
        A.set_right(B)
        A.set_parent(B.get_parent())
        if A.get_parent() !=None :
            if A.get_parent().get_left().get_key() == B.get_key():
                A.get_parent().set_left(A)
            else:
                A.get_parent().set_right(A)
        B.set_parent(A)

    """preforms a left rotation on given node 
       Complexity : O(1)
    @type avl_node: AVLNode
    @param avl_node: node to be rotated
    
    """

    def left_rotation(avl_node):   # the function performs a Left rotation on 3 nodes as demonstrated in class
        B = avl_node
        A = avl_node.get_right()
        B.set_right(A.get_left())
        B.get_right().set_parent(B)
        A.set_left(B)
        A.set_parent(B.get_parent())
        if A.get_parent() !=None :
            if A.get_parent().get_left().get_key() == B.get_key():
                A.get_parent().set_left(A)
            else:
                A.get_parent().set_right(A)
        B.set_parent(A)

    """updates changed fields (used for insertions and deletions) 
       Complexity : O(1)
    @type avl_node: AVLNode
    @param avl_node: node to be updated
    
    """
    
    def fields_update(avl_node):        
        avl_node.set_size(1+avl_node.get_left().get_size() + avl_node.get_right().get_size())   
        avl_node.set_height(1+max(avl_node.get_left().get_height(), avl_node.get_right().get_height() ))
        avl_node.set_bfs((avl_node.get_left().get_height())-avl_node.get_right().get_height())



"""
A class implementing an AVL tree.
"""

class AVLTree(object):

    """
    Constructor, you are allowed to add more fields.  

    """
    def __init__(self):
        self.root = AVLNode(None,None)      # we initialize a tree by creating a non-real node to be its root


    def set_root(self, new_root):
        self.root= new_root

    """searches for a node in the dictionary corresponding to the key
       Complexity : O(log(n))
    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: node corresponding to key
    """
    def search(self, key):                  
        x= self.get_root()
        if(x.is_real_node()==False):         # the case in which the tree is empty 
            return None
        while x.get_key()!=None :
        
            if key== x.get_key() :
                return x
            
            else:
                if key<x.get_key() :
                    
                        x=x.get_left()
                    
                else:
                    x=x.get_right()

        if(x.get_key()!=key):               # in case we searched the whole tree and did not find the desired key we return None
            return None
        return x

    """inserts a given node as leaf into a tree
       Complexity : O(log(n))
    @type avl_node_1: AVLNode
    @param avl_node_1: node to be inserted 
    
    """


    def insert_as_leaf(self,avl_node_1):     
        if self.get_root().get_key()==None:               # in case the tree is empty we set the node to be the root of the tree 
            self.set_root(avl_node_1)
            self.get_root().set_size(1)
            self.get_root().set_height(0)
            self.get_root().get_left().set_parent(avl_node_1)
            self.get_root().get_right().set_parent(avl_node_1)

        else:                              
            y = None
            x = self.get_root()
            while(x.get_key()!= None):                   # searching trough the tree in O(log(n)) to find the right place to attach the node as a leaf 
                y = x
                if avl_node_1.get_key() < x.get_key():
                    x = x.get_left()
                else:
                    x = x.get_right()
            
            avl_node_1.set_parent(y)
            avl_node_1.set_height(0)     
            if y == None:
                self.set_root(avl_node_1) 
            else:
                if avl_node_1.get_key() > y.get_key():
                    y.set_right(avl_node_1)
                else:
                    y.set_left(avl_node_1)
        z=avl_node_1
        z.get_left().set_parent(z)
        z.get_right().set_parent(z)
        z.set_size(1)
            

    """preforms a right rotation on given node while updating its fields
       Complexity : O(1)
    @type z: AVLNode
    @param z: node to be rotated
    
    """
    def one_R_rotation(self,z):              
        if self.get_root().get_key()==z.get_key():
            self.set_root(z.get_left())
        temp1=z.get_left()
        z.right_rotation()
        z.fields_update()
        temp1.fields_update()

    """preforms a left rotation and then a right rotation on given node while updating its fields
       Complexity : O(1)
    @type z: AVLNode
    @param z: node to be rotated
    
    """
            
    def L_rotation_R_rotation(self,z):     
        if self.get_root().get_key()==z.get_key():
            self.set_root(z.get_left().get_right())    
        temp1=z.get_left()
        temp2=z.get_left().get_right()
        z.get_left().left_rotation()
        temp1.fields_update()
        temp2.fields_update()
        temp3=z.get_left()
        z.right_rotation()
        z.fields_update()
        temp3.fields_update()

    """preforms a left rotation on given node while updating its fields
       Complexity : O(1)
    @type z: AVLNode
    @param z: node to be rotated
    
    """

    def one_L_rotation(self,z):      
        if self.get_root().get_key()==z.get_key():
            self.set_root(z.get_right())
        temp1=z.get_right()
        z.left_rotation()
        z.fields_update()
        temp1.fields_update()

    """preforms a right rotation and then a left rotation on given node while updating its fields
       Complexity : O(1)
    @type z: AVLNode
    @param z: node to be rotated
    
    """
        
    def R_rotation_L_rotation(self,z):    
        if self.get_root().get_key()==z.get_key():
            self.set_root(z.get_right().get_left()) 							
        tem1=z.get_right()
        tem2=z.get_right().get_left()
        z.get_right().right_rotation()
        tem1.fields_update()
        tem2.fields_update()
        temp3=z.get_right()
        z.left_rotation()
        z.fields_update()
        temp3.fields_update()
 

    """inserts a new node into the dictionary with corresponding key and value
       Complexity : O(log(n))
    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """
    def insert(self, key, val):               
        avl_node_1= AVLNode(key,val)         
        self.insert_as_leaf(avl_node_1)     # inserting  the node as a leaf in O(log(n)) 

        z= avl_node_1.get_parent()                   
        rotation_counter=0                 # the number of rotations needed to keep the tree balanced
        height_change_counter=0

        while z!=None:                     # going through the nodes in the path from the attached node to the root , in order to find AVL criminals and perform rotations if needed
            next_z=z.get_parent()
            first_height=z.get_height()

            z.fields_update()             # updating the fields of the nodes in the path from the attached node to the root

            if abs(z.get_bfs())<2 and z.get_height()==first_height:
                z=next_z
                
            else:
                if abs(z.get_bfs())<2 and z.get_height()!=first_height :
                    height_change_counter +=1
                    z=next_z
                else:
                    if z.get_bfs()==2 :
                        if z.get_left().get_bfs()==1 :
                            self.one_R_rotation(z)
                            rotation_counter=1
                            z=next_z
                        else:
                            if z.get_left().get_bfs()==-1 :
                                
                                self.L_rotation_R_rotation(z)
                                rotation_counter=2
                                z=next_z
                    else:
                        if z.get_bfs()==-2 :
                            if z.get_right().get_bfs()==-1 :
                                
                                self.one_L_rotation(z)
                                rotation_counter=1
                                z=next_z
                            else:
                                if z.get_right().get_bfs()==1:
                                    self.R_rotation_L_rotation(z)
                                    rotation_counter=2
                                    z=next_z
        
        return rotation_counter + height_change_counter

    """finds the node with the minimal key of given subtree
       Complexity : O(log(n))
    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: node
    @returns: the node with minimal key of given subtree
    """
    def minimal_key_node(self,node):    
    
        current = node
 
        while current.get_left().get_key() != None :     # going through the left side of the tree in O(log(n))
            current = current.get_left()
        
        return current

    """finds the successor of given node
       Complexity : O(log(n))
    @type n: AVLNode
    @pre: n is a real pointer to a node in self
    @rtype: node
    @returns: the successor of given node
    """
    def find_successor(self, n):

        if n.get_right() != None :
            return self.minimal_key_node(n.get_right())
        
        p = n.get_parent()

        while p != None and n == p.get_right() :   # finding the successor of a given node in O(log(n)) as demonstrated in class 
            n = p
            p = n.get_parent()
        
        return p
    
    """deletes a node as in BST
       Complexity : O(log(n))
    @type n: node
    @pre: n is a real pointer to a node in self
    @rtype: node
    @returns: parent of physically deleted node
    """
    
    def deleteAsUsual(self, node):      

        
        if node.get_left().get_key()==None and node.get_right().get_key()==None:   # the case in which the node is a leaf 

            if self.get_root()==node:
                self.set_root(AVLNode(None,None))
                return None

            if node.get_parent().get_right()==node:
                node.get_parent().set_right(AVLNode(None,None))
                return node.get_parent()
            else:
                node.get_parent().set_left(AVLNode(None,None))
                return node.get_parent()

        elif node.get_right().is_real_node() and not (node.get_left().is_real_node())  :    # the case in which the node has only a right child
            if self.get_root()==node:
                self.set_root(node.get_right())
                node.get_right().set_parent(None)
                return node.get_parent()

            elif node.get_parent().get_right()==node:
                node.get_parent().set_right(node.get_right())
                node.get_right().set_parent(node.get_parent())
                return node.get_parent()
            else:
                node.get_parent().set_left(node.get_right())
                node.get_right().set_parent(node.get_parent())
                return node.get_parent()
                
        elif node.get_left().is_real_node() and not (node.get_right().is_real_node()) :   # the case in which the node has only a left child 

            if self.get_root()==node:
                self.set_root(node.get_left())
                node.get_left().set_parent(None)
                return node.get_parent()

            elif node.get_parent().get_right()==node:
                node.get_parent().set_right(node.get_left())
                node.get_left().set_parent(node.get_parent())
                return node.get_parent()
            else:
                node.get_parent().set_left(node.get_left())
                node.get_left().set_parent(node.get_parent())
                return node.get_parent()

        else:                           # the case in which the node has two children 
            y=self.find_successor(node)      # the successor will be the actual node deleted from the tree , finding him in O(log(n))
            node.set_key(y.get_key())
            node.set_value(y.get_value())

            if y.get_parent().get_right()==y:
                y.get_parent().set_right(y.get_right())
                y.get_right().set_parent(y.get_parent())
                return y.get_parent()

                
            else:
                y.get_parent().set_left(y.get_right())
                y.get_right().set_parent(y.get_parent())
                return y.get_parent()


    """deletes node from the dictionary
       Complexity : O(log(n))
    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node):

        y=self.deleteAsUsual(node)      # y is the parent of the physically deleted node 

        rotation_counter=0
        height_counter=0

        while y!=None :             # going through the nodes in the path from the deleted node to the root , in order to find AVL criminals and perform rotations if needed in O(log(n))
            next_y= y.get_parent()
            prev_height=y.get_height()
            y.fields_update()
            
            if abs(y.get_bfs())<2  and y.get_height()==prev_height:
                y= next_y
            else:
                if abs(y.get_bfs())<2  and y.get_height()!=prev_height:
                    height_counter+=1
                    y=next_y
                else:
                    if y.get_bfs()==2 :
                        if y.get_left().get_bfs()==1 :
                            self.one_R_rotation(y)
                            rotation_counter+=1
                            y=next_y
                        else:
                            if y.get_left().get_bfs()==-1 :
                                
                                self.L_rotation_R_rotation(y)
                                rotation_counter+=2
                                y=next_y
                            else:
                                if y.get_left().get_bfs()==0:
                                    self.one_R_rotation(y)
                                    rotation_counter+=1
                                    y=next_y
                    else:
                        if y.get_bfs()==-2 :
                            if y.get_right().get_bfs()==-1 :
                                
                                self.one_L_rotation(y)
                                rotation_counter+=1
                                y=next_y
                            else:
                                if y.get_right().get_bfs()==1:
                                    self.R_rotation_L_rotation(y)
                                    rotation_counter+=2
                                    y=next_y
                                else:
                                    if y.get_right().get_bfs()==0:
                                        self.one_L_rotation(y)
                                        rotation_counter+=1
                                        y=next_y
        return     rotation_counter+height_counter


    """returns an array representing dictionary 
       Complexity : O(n)
    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """
    def avl_to_array(self):                    # gathering all the keys and the values in to an array in O(n) using the inorder search
        """inner func: returns an array representing dictionary
            Complexity: O(n)
            @type avl_node: AVLNode
            @rtype: list
            @returns: a sorted list according to key of touples (key, value) representing the data structure
        """
        def array_node_connected(avl_node):
            if(avl_node.get_key()==None):
                return []
            return array_node_connected(avl_node.get_left()) +[(avl_node.get_key(),avl_node.get_value())] +array_node_connected(avl_node.get_right())

        return array_node_connected(self.get_root())


    """returns the number of items in dictionary 
       Complexity : O(1)
    @rtype: int
    @returns: the number of items in dictionary 
    """
    def size(self):
        return self.get_root().get_size()

    """compute the rank of node in the dictionary
       Complexity : O(log(n))
    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary to compute the rank for
    @rtype: int
    @returns: the rank of node in self
    """
    def rank(self, node):                  # finding the rank of a giving node in O(log(n)) as demonstrated in class 
        count=node.get_left().get_size()+1
        curr=node
        if(curr==self.get_root()):
            return count

        while curr!=self.get_root():
            if curr==curr.get_parent().get_right():
                count=count+curr.get_parent().get_left().get_size()+1
            curr=curr.get_parent()

        return count
                



    """finds the i'th smallest item (according to keys) in the dictionary
       Complexity : O(log(n))
    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @rtype: AVLNode
    @returns: the node of rank i in self
    """
    def select(self, i):            # finding the node with rank = i  in O(log(n)) as demonstrated in class
        """inner func, finds the i'th smallest item (according to keys) in the dictionary
       Complexity : O(log(n))
    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @type avl_node: AVLNode
    @rtype: AVLNode
    @returns: the node of rank i in self
        """
        def Tree_select_rec(avl_node,i):
            r = avl_node.get_left().get_size() +1
            if i==r :
                return avl_node
            else:
                if i<r:
                    return Tree_select_rec(avl_node.get_left(),i)
                else:
                    return Tree_select_rec(avl_node.get_right(),i-r)
        return Tree_select_rec(self.get_root(),i)
    
        
        


    """finds the node with the largest value in a specified range of keys
       Complexity : O(min{(b-a),n})
    @type a: int
    @param a: the lower end of the range
    @type b: int
    @param b: the upper end of the range
    @pre: a<b
    @rtype: AVLNode
    @returns: the node with maximal (lexicographically) value having a<=key<=b, or None if no such keys exist
    """
    
    
    def max_range(self, a, b):
        """inner func, finds the node with the largest value in a specified range of keys
       Complexity : O(min{(b-a),n})
    @type avl_nodes: AVLNode
    @type a: int
    @param a: the lower end of the range
    @type b: int
    @param b: the upper end of the range
    @pre: a<b
    @rtype: AVLNode
    @returns: the node with maximal (lexicographically) value having a<=key<=b, or None if no such keys exist
        """
        
        def nodes_to_max_range_array(avl_node,a,b):    # gathering all the nodes with a< keys < b in O(min{(b-a),n}) 
          
            if avl_node.get_key()==None:
                return []
            if(avl_node.get_key()>b):
                return nodes_to_max_range_array(avl_node.get_left(),a,b)
            if(avl_node.get_key()<a):
                return nodes_to_max_range_array(avl_node.get_right(),a,b)
            if(avl_node.get_key()>=a and avl_node.get_key()<=b):
                return [[avl_node,avl_node.get_value()]] + nodes_to_max_range_array(avl_node.get_left(),a,b) + nodes_to_max_range_array(avl_node.get_right(),a,b)
        range_array=nodes_to_max_range_array(self.get_root(),a,b)
        max = range_array[0]
        for pair in range_array:
            if pair[1]> max[1]:
                max= pair
        return max[0]


    """returns the root of the tree representing the dictionary
       Complexity : O(1)
    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """
    def get_root(self):
        return self.root

    




