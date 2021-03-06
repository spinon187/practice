const getLLSum = head => {
  let curr = head, expo = 0, op = 0;
  while(curr){
    op += curr.val*(10**expo)
    expo++;
    curr = curr.next
  }
  return op
}

var addTwoNumbers = function(l1, l2) {
  let v1 = getLLSum(l1),
  v2 = getLLSum(l2),
  finalSum = v1+v2;
  console.log(finalSum, v1, v2)
  let newLLHead = new ListNode(), curr = newLLHead;
  while(finalSum){
    let nextVal = finalSum%10;
    curr.val = nextVal;
    finalSum = (finalSum - nextVal)/10
    if(finalSum){
      curr.next = new ListNode();
      curr = curr.next;
    }
  }
  return newLLHead
};

const getLLSum = head => {
  let curr = head, op = [];
  while(curr){
    op.push(curr.val);
    curr = curr.next
  }
  return op
}

var addTwoNumbers = function(l1, l2) {
  let v1 = getLLSum(l1),
  v2 = getLLSum(l2),
  i = 0,
  newLLHead = new ListNode(),
  curr = newLLHead;
  while(i < v1.length || i < v2.length){
    let newVal = (v1[i] || 0) + (v2[i] || 0);
    if(newVal >= 10){
      newVal = newVal%10;
      if(i+1 > v1.length){
        v1.push(1)
      } else {
        v1[i+1]++
      }
    }
    curr.val = newVal;
    i++
    if(i < v1.length || i < v2.length){
      curr.next = new ListNode();
      curr = curr.next;
    }
  }
  return newLLHead
};

const addTwoNumbers = (l1, l2) => {
  let newHead = new ListNode(), curr = newHead, carriedOne = false;
  while(l1 || l2){
    let newVal = 0;
    if(l1) newVal += l1.val;
    if(l2) newVal += l2.val;
    if(carriedOne){
      newVal += 1;
      carriedOne = false
    }
    if(newVal > 9){
      newVal = newVal%10;
      carriedOne = true
    }
    curr.val = newVal;
    l1 = l1.next ? l1.next : null;
    l2 = l2.next ? l2.next : null;
    if(l1 || l2){
      curr.next = new ListNode();
      curr = curr.next;
    } else if(carriedOne){
      curr.next = new ListNode();
      curr.next.val = 1;
    }
  }
  return newHead
}