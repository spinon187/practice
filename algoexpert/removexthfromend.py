# This is an input class. Do not edit.
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None


def removeKthNodeFromEnd(head, k):
  length = 1
	curr = head
	while curr.next is not None:
		length += 1
		curr = curr.next
	target = length - k
	if target == 0:
		head.value = head.next.value
		head.next = head.next.next
		return
	curr = head
	countdown = 1
	while countdown < target:
		curr = curr.next
		countdown += 1
	if curr.next.next is None:
		curr.next = None
	else:
		curr.next = curr.next.next