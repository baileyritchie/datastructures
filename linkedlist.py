class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    # starts with a head pointing to none
    self.head = None
  def size(self):
    count = 0
    start = self.head
    while start:
      #while self.head is not none
      count+=1
      start = start.next
    return count

  def __empty__(self):
    if self.head is not None:
      return False
    else:
      return True

  def push_front(self,val):
    #appends at the very front, makes the next point to the current head
    new_node = Node(val)
    new_node.next = self.head
    self.head = new_node
    
  def value_at(self,index):
    """ returns the value of the nth item (starting at 0 for first)
    """
    count = 0
    curr = self.head
    while curr:
      if count == index:
        return curr.data
      curr = curr.next
      count +=1
    return IndexError('index is out of bounds')
  def find(self,val):
    """ returns the index of the first appearance of a value"""
    curr = self.head
    count = 0
    while curr:
      if curr.data == val:
        return count
      count +=1
      curr = curr.next
    return IndexError('Value could not be found')
  def pop_front(self):
    """ removes the front node and returns its value"""
    if self.head.next:
      # if there is more than one node
      front = self.head.data
      new_head = self.head.next
      self.head = new_head
      return front
    else: 
      self.head = None
      # set the head to none, there is no more linkedlist
  
  def push_back(self,value):
    """ adds an item to end of the linked list"""
    curr = self.head
    new_node = Node(value)
    while curr:
      if curr.next is None:
        curr.next = new_node
        break
      curr = curr.next  

 
  def pop_back(self):
    """ removes an item from end and returns its value"""
    curr = self.head
    
    while curr:
      if curr.next.next is None:
        # 2 before end
        back = curr.next.data
        curr.next = None
        break
      curr = curr.next
    return back

  def front(self):
    """ get value of front item """
    return self.head.data

  
  def back(self):
    """ get value of last item """
    curr = self.head
    while curr:
      if curr.next.next == None:
        # on last item
        return curr.next.data
      curr = curr.next 
  
  def insert(self,index,value):
    #insert value at index, so current item at that index is pointed to by new item at index
    new_node = Node(value)
    curr = self.head
    prev= self.head.next
    count = 0
    while curr:
      print('current node data:',curr.data)
      if count == index:
        print('count is:',count,'index is:',index)
        new_node.next = curr.next
        curr.next = new_node
        break
      count+=1
      curr = curr.next

  
  def erase(self,index):
    """removes node at given index"""
    curr = self.head
    if index == 0:
      # if this is the head that needs to be removed
      self.head = curr.next
      curr = None
      return
    prev = None
    count = 0 
    while curr and count != index:
      prev = curr
      curr = curr.next
      count +=1
    if curr is None:
      return 
    prev.next = curr.next
    curr = None

  """
  def value_n_from_end(self,n):

  def reverse(self):
  """

  def remove_value(self,value):
    """removes the first item in the list with this value"""
    curr = self.head
    if curr.data == value:
      # if this is the head that needs to be removed
      self.head = curr.next
      curr = None
      return
    prev = None
    while curr and curr.data != value:
      prev = curr
      curr = curr.next
    if curr is None:
      return 
    prev.next = curr.next
    curr = None



ll = LinkedList()
ll.push_front(88) #4
ll.push_front(12) #3
ll.push_front(3) #2
ll.push_front(76) #1
ll.push_front(44) #0

print('size:',ll.size())
ll.push_back(24) #5
print('size:',ll.size())
print('should be popped:',ll.pop_back())
print('size:',ll.size())
ll.insert(2, 65)
print('size:',ll.size())
print(ll.value_at(4))
#ll.erase(4)
ll.remove_value(88)
print('size:',ll.size())
print(ll.value_at(4))
