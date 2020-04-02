var getIntersectionNode = function(headA, headB) {
  let d = new Set(), currA = headA, currB = headB, found = null;
  while(!found && (currA || currB)){
    if(currA){
      if(d.has(currA)){
        found = currA;
      } else {
        d.add(currA);
        currA = currA.next
      }
    }
    if(currB){
      if(d.has(currB)){
        found = currB;
      } else {
        d.add(currB);
        currB = currB.next
      }
    }
  }
  return found;
};