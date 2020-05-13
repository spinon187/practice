class Node {
  constructor(val){
    this.val = val;
    this.prereqs = [];
  }
}

const traverse = (node, set) => {
  let canTake = true;
  node.prereqs.forEach(n => {
    if(canTake){
      if(!set.has(n)){
        canTake = traverse(n, set)
      }
    }
  })
  if(canTake){
    set.add(node);
    return true;
  }
  else {
    return false;
  }
}

var canFinish = function(numCourses, pr) {
  let k = {}, taken = new Set();
  for(let i = 0; i<numCourses; i++){
    let nn = new Node(i);
    k[i] = nn;
  }
  for(let i = 0; i<pr; i++){
    k[pr[i][0]].prereqs.push(k[pr[i][1]])
  }
  let j = 0, op = true;
  while(j<numCourses && op){
    op = traverse(k[j], taken)
    j++
  }
  return op
};