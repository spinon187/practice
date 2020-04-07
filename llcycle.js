var hasCycle = function(head) {
  let visited = new Set(), curr = head, cycle = false;
  while(curr && !cycle){
    if(visited.has(curr.next)){
      cycle = true;
    }
    visited.add(curr);
    curr = curr.next
  }
    return cycle
};