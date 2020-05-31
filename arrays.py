## Arrays Data Structure based on C compatible data types

import ctypes

class DynamicArray(object):
  def __init__(self):
    self.n = 0
    self.capacity = 1
    self.A = self.make_array(self.capacity)

  def __len__(self):
    return self.n

  def is_empty(self):
    if len(self.A) <=1:
      return True
    return False

  def __getitem__(self,k):
    if not 0 <= k <self.n:
      IndexError('k is out of bounds')
    return self.A[k]

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
    if 0 < index or index >= self.n:
      IndexError('index out of bounds')
    i = index
    for elm in range(i,self.n-1):
      self.A[elm] = self.A[elm+1]
    self.n -=1
    self._resize(self.n)
  def at(self,index):
    return self.A[index]

  def make_array(self,new_cap):
    return (new_cap * ctypes.py_object)()
  
arr = DynamicArray()

arr.append(3) #0
arr.append(2) #1
arr.append(45) #2
arr.append(111) #3
print(len(arr)) # should be 4
print(arr.at(2)) # should be 45
arr.delete(2) 
print(arr.at(2)) # should be 111
print(len(arr)) # should be 3
