def shiftLinkedList(head, k):
  l = 1
  tail = head
  while tail.next:
    tail = tail.next
    l += 1
  diff = abs(k) % l
  if diff == 0:
    return head
  if k > 0:
    diff = l - diff
  newTail = head
  while diff > 1:
    newTail = newTail.next
    diff -= 1
  newHead = newTail.next
  newTail.next = None
  tail.next = head
  return newHead

# This is the class of the input linked list.
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None