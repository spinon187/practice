var deleteDuplicates = function(head) {
  // let dict = new Set(), dummy = new ListNode(-1);
  // dummy.next = head;
  // let curr = head, prev = dummy;
  // while(curr){
  //     if(!dict.has(curr.val)){
  //         dict.add(curr.val)
  //         prev = curr;
  //         curr = curr.next;
  //     } else {
  //         prev.next = curr.next;
  //         curr = curr.next;
  //     }
  // }
  // return head;
  let curr = head;
  while(curr && curr.next){
      if(curr.val === curr.next.val){
          curr.next = curr.next.next;
      } else {
          curr = curr.next;
      }
  }
  return head;
};