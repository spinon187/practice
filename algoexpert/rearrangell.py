def rearrangeLinkedList(head, k):
  smallHead, smallTail = None, None
  evenHead, evenTail = None, None
  bigHead, bigTail = None, None
  
  node = head
  while node is not None:
    if node.value < k:
      smallHead, smallTail = extendList(smallHead, smallTail, node)
    elif node.value > k:
      bigHead, bigTail = extendList(bigHead, bigTail, node)
    else:
      evenHead, evenTail = extendList(evenHead, evenTail, node)
    prev = node
    node = node.next
    prev.next = None
  
  finalHead = None
  if smallHead:
    finalHead = smallHead
    if evenHead:
      smallTail.next = evenHead
    else:
      smallTail.next = bigHead
  if evenHead:
    if finalHead is None:
      finalHead = evenHead
    if bigHead:
      evenTail.next = bigHead
  if bigHead and finalHead is None:
    finalHead = bigHead
  
  return finalHead
  

def extendList(head, tail, node):
  if head is None:
    head = node
    tail = node
  else:
    tail.next = node
    tail = node
  return [head, tail]


# This is the class of the input linked list.
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None