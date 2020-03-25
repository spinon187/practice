var deleteNode = function(node) {
  curr = node;
  while(curr){
    curr.val = curr.next.val
    if(curr.next.next){
      curr = curr.next;
    } else {
      curr.next = null;
      curr = null;
    }
  }
};