def reverseLinkedList(head):
  curr = head
  prev = None
  while(curr):
    flip = curr.next
    curr.next = prev
    prev = curr
    curr = flip
  return prev