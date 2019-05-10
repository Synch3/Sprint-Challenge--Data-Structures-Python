class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0 % self.capacity
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    self.current = (self.current+1) % self.capacity

  def get(self):
    if self.current > self.capacity:
      return self.storage
    else:
       return list(filter(None.__ne__, self.storage))