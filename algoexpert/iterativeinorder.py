def iterativeInOrderTraversal(tree, callback):
  prev = None
  curr = tree
  while curr is not None:
    if not prev or prev == curr.parent:
      if curr.left:
        nxt = curr.left
      else:
        callback(curr)
        nxt = curr.right if curr.right else curr.parent
    elif prev == curr.left:
      callback(curr)
      nxt = curr.right if curr.right else curr.parent
    else:
      nxt = curr.parent
    prev = curr
    curr = nxt