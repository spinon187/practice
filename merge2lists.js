var mergeTwoLists = function(l1, l2) {
  if(!l1) return l2;
  if(!l2) return l1;
  let left = l1.val<=l2.val ? l1 : l2, right = l1.val>l2.val ? l1 : l2;
  // [1,2,4]
  // [1,3,4]
  let curr = new ListNode(-1), fakeHead = curr;

  while(curr){ //1, 1
      let smaller = left.val <= right.val ? left : right, //l1 1 | l2 1
      bigger = smaller === left ? right : left; //l2 1 | l1 2
      if(bigger == smaller){
        let next = smaller.next;
        let next2 = bigger.next;
        curr.next = smaller;
        curr.next.next = bigger;
        left = next;
        right = next2;
        curr = curr.next.next;
      } else {
        next = smaller.next;
        curr.next = smaller;
        next = left;
        bigger = right;
        curr = curr.next;
      }

  }
  return fakeHead.next;
};