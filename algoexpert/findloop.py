# This is an input class. Do not edit.
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None


def findLoop(head):
  fast = head.next.next
  slow = head.next
  while fast != slow:
    slow = slow.next
    fast = fast.next.next
  slow = head
  while fast != slow:
    fast = fast.next
    slow = slow.next
  return fast