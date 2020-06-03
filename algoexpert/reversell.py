def reverseLinkedList(head):
  curr = head.next
  prev = head
  while(curr):
    flip = curr.next
    curr.next = prev
    prev = curr
    curr = flip
  head.next = None
  return prev