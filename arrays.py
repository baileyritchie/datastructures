## Arrays Data Structure based on C compatible data types

import ctypes

class DynamicArray(object):
  def __init__(self):
    self.n = 0
    self.capacity = 1
    self.A = self.make_array(self.capacity)

  def __len__(self):
    return self.n
  def __capacity__(self):
    return self.capacity
  def is_empty(self):
    if len(self.A) <=1:
      return True
    return False
  def __getitem__(self,k):
    if not 0 <= k <self.n:
      IndexError('k is out of bounds')
    return self.A[k]

  def prepend(self,element):
    self._resize(self.n+1)
    i = self.n
    while i > 0:
      self.A[i] = self.A[i-1]
      i-=1
    self.A[0] = element
    self.n +=1 

  def append(self,element):
    if self.n == self.capacity:
      #if it reaches its maximum
      self._resize(2*self.capacity)
    self.A[self.n] = element #reset the last index to hold the new element
    self.n+=1

  def _resize(self,new_cap):
    if self.n < new_cap and self.n == self.capacity:
      #increasing size
      # temporarily make a new array 
      B = self.make_array(new_cap)
      for k in range(self.n):
        B[k] = self.A[k] # making a copy and reffing the elements of B from A
      self.A = B
      self.capacity = new_cap
    elif self.n > new_cap and self.n == self.capacity:
      # need to shrink
      B = self.make_array(new_cap)
      for k in range(new_cap):
        B[k] = self.A[k]
      self.A = B
      self.capacity = new_cap

  def pop(self):
    last = self.A[self.n-1]
    self.n-=1
    return last

  def insert(self,index,item):
    if 0 < index or index> self.n:
      IndexError('index out of bounds')
    self._resize(self.n+1)
    i = self.n
    while i > index:
      self.A[i] = self.A[i-1]
      i-=1
    self.A[index] = item
    self.n +=1

  def delete(self, index):
    if 0 < index or index > self.n:
      IndexError('index out of bounds')
    i = index
    for elm in range(i,self.n-1):
      self.A[elm] = self.A[elm+1]
    self.n -=1
    self._resize(self.n)
  
  def at(self,index):
    return self.A[index]

  def find(self,item):
    i=0
    while i < self.n:
      if self.A[i] == item:
        return i
      else:
        i+=1
    return -1
  
  def remove(self,item):
    # looks for value and removes index holding it (even if in multiple places)
    i=0
    while i <= self.n:
      print(i,'remove list value:',self.A[i])
      if self.A[i] == item and i != self.n:
        print('i before del:',i)
        self.delete(i)
        i-=1
        print('i after del:',i)
      if self.A[i] == item and i == self.n:
        #if end of the list, the delete method does not work use pop method
        print('self.n before pop:',self.n,'and val to be popped ',self.A[i])
        self.n-=1
        self._resize(self.n)
        print('self.n after pop:',self.n)
      else:
        i+=1
  def print_loop(self):
    for i in range(self.n+3#):
      print(self.A[i])

  def make_array(self,new_cap):
    return (new_cap * ctypes.py_object)()
  
arr = DynamicArray()

arr.append(3) #0
arr.append(2) #1
arr.append(45) #2
arr.append(111) #3
arr.append(45) #4
#arr.pop()
#arr.append(66) #5
#print(len(arr)) # should be 4
#print(arr.at(3)) # should be 45
#arr.delete(3) 
#print(arr.at(3)) # should be 111
#print(len(arr)) # should be 3
#arr.prepend(4)
#print(arr.at(4)) # should be 2
#print(arr.find(111))
print(arr.at(2)) #should be 45
print('length before remove:',len(arr))
arr.remove(45)
print('len after remove:',len(arr))
print(arr.at(2)) # should be 111
#print('at index 3 and 4:',arr.at(3),arr.at(4)) # should not exist
#arr.print_loop()

