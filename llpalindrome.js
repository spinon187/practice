/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
  if(!head || !head.next) return true;
  let q = [], curr = head;
  while(curr){
    q.push(curr.val);
    curr = curr.next;
  }
  let m = ~~(q.length/2), failed = false, i = 0;
  while(i<m && !failed){
      e = q.pop()
    if(q[i] !== e){
      failed = true;
    }
    i++
  }
  return !failed;
};