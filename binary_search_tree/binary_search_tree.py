class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      #lesser on left, greater on right
   if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
   elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
        return True
    if target < self.value :
      if not self.left:
        pass # do nothing because it is recursive loop
      else:
        if self.left.contains(target):
          return True

    elif target > self.value:
      if not self.right:
        pass
      else:
        if self.right.contains(target) :
          return True

  def get_max(self):
    if self.right is None:
      return self.value
    else:
      return self.right.get_max()

  def for_each(self, cb):
    cb(self.value)
    
    if self.left:
      self.left.for_each(cb)
    
    if self.right:
      self.right.for_each(cb)