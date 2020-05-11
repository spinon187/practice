class Node {
  constructor(val){
    this.val = val;
    this.prereqs = [];
  }
}

const traverse = (node, )

var canFinish = function(numCourses, pr) {
  let k = {}, taken = new Set();
  for(let i = 0; i<numCourses; i++){
    let nn = new Node(i);
    k[i] = nn;
  }
  for(let i = 0; i<pr; i++){
    k[pr[i][0]].prereqs.push(k[pr[i][1]])
  }
  

};