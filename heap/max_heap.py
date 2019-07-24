class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)

    #bubble_up checks if its parent is larger and swap if so
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    pass

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1) // 2

      # is current element larger than parent
      if self.storage[index] > self.storage[parent]:
        #if so swap
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent
      else:
        break

  def _sift_down(self, index):
    pass
