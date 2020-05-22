class Node {
  constructor(val){
    this.val = val;
    this.prereqs = [];
  }
}

const traverse = (node, taken, visited) => {
  visited.add(node);
  let canTake = true;
  node.prereqs.forEach(n => {
    if(!visited.has(n) && canTake){
      if(!taken.has(n)){
        canTake = traverse(n, taken, visited)
      }
    }
  })
  if(canTake){
    taken.add(node);
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
  for(let i = 0; i<pr; i++){
    if(!k[i].prereqs){
      taken.add(k[i])
    }
  }

  let j = 0, op = true;
  while(j<numCourses && op){
    op = traverse(k[j], taken)
    j++
  }
  return op
};