class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
  if headOne.value < headTwo.value:
    newHead = headOne
    last = headOne
    currOne = headOne.next
    currTwo = headTwo
  else:
    newHead = headTwo
    last = headTwo
    currOne = headOne
    currTwo = headTwo.next
  while currOne and currTwo:
    if currOne.value < currTwo.value:
      last.next = currOne
      last = currOne
      currOne = last.next
    else:
      last.next = currTwo
      last = currTwo
      currTwo = last.next
  if currOne and not currTwo:
    last.next = currOne
  elif currTwo and not currOne:
    last.next = currTwo
  return newHead