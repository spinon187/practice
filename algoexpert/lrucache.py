# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
  def __init__(self, maxSize):
    self.maxSize = maxSize or 1
    self.cache = {}
    self.size = 0
    self.order = DLL()

  def insertKeyValuePair(self, key, value):
    if key not in self.cache:
      if self.size == self.maxSize:
        self.evict()
      else:
        self.size += 1
      self.cache[key] = DLLNode(key, value)
    else:
      self.updateKey(key, value)
    self.updateRecent(self.cache[key])

  def getValueFromKey(self, key):
    if key not in self.cache:
      return None
    self.updateRecent(self.cache[key])
    return self.cache[key].value

  def getMostRecentKey(self):
    if self.order.head is None:
      return None
    return self.order.head.key
  
  def evict(self):
    target = self.order.tail.key
    self.order.removeTail()
    del self.cache[target]
    
  def updateRecent(self, node):
    self.order.setHead(node)
    
  def updateKey(self, key, value):
    self.cache[key].value = value

  
class DLL:
  def __init__(self):
    self.head = None
    self.tail = None
  def setHead(self, node):
    if self.head == node:
      return
    elif self.head is None:
      self.head = node
      self.tail = node
    elif self.head == self.tail:
      self.tail.prev = node
      self.head = node
      self.head.next = self.tail
    else:
      if self.tail == node:
        self.removeTail()
      node.unbind()
      self.head.prev = node
      node.next = self.head
      self.head = node
  def removeTail(self):
    if self.tail is None:
      return
    if self.tail == self.head:
      self.head = None
      self.tail = None
      return
    self.tail = self.tail.prev
    self.tail.next = None
      
      

class DLLNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None
    
  def unbind(self):
    if self.prev is not None:
      self.prev.next = self.next
    if self.next is not None:
      self.next.prev = self.prev
    self.prev = None
    self.next = None