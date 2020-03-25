var removeElements = function(head, val) {
  let dummy = new ListNode(-1);
  dummy.next = head;
  curr = dummy;
  while(curr){
      if(curr.next && curr.next.val === val){
          curr.next = curr.next.next;
 
      } else {
          curr = curr.next;
      }
      
  }
  return dummy.next;
};