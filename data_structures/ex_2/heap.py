def heapsort(arr):
    # initialize an empty heap
    heap = Heap()
    # initialize a list to hold all of our sorted output
    sorted = [0] * len(arr)
    # loop over all elements in arr
        for el in arr:
    # insert each element into the heap
            heap.insert(el)
    # loop over all elements in arr
        for i in range(len(arr)):
    # call heap.delete
    # store the deleted element in the sorted list in the proper order
            sorted[len(arr) - i - 1] = heap.delete()
            # instead of sorted[i] = heap.delete() -> sorted.reverse()
    # return the sorted list
        return sorted

 

class Heap:
  def __init__(self):
    self.storage = []
    def depth_first_for_each(self, cb):
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2