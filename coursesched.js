class Node {
  constructor(val){
    this.val = val;
    this.prereqs = [];
    this.remaining = 0
  }
}

class Graph {
  constructor(){
    this.graph = {}
    this.nodes = []
  }

  addNode = val => {
    this.graph[val] = new Node(val);
    this.nodes.push(val)
  }

  addPrereq = (val, pre) => {
    let node = this.graph[val],
    dep = this.graph[pre];
    node.prereqs.push(dep.val);
    dep.remaining++
  }
}

const traverse = graph => {
  let cleared = [], free = [];
  for(let i = 0; i < graph.nodes.length; i++){
    let node = graph.nodes[i]
    if(!graph.graph[node].remaining){
      free.push(node)
    }
  }
  while(free.length){
    let freeNode = free.pop()
    graph.graph[freeNode].prereqs.forEach(prereq => {
      graph.graph[prereq].remaining--
      if(!graph.graph[prereq].remaining) free.push(graph.graph[prereq].val)
    })
    cleared.push(freeNode)
  }
  return cleared
}

const canFinish = (numCourses, prereqs) => {
  let graph = new Graph(numCourses)
    for(let i = 0; i<numCourses; i++){
      graph.addNode(i)
    }
  for(let i = 0; i<prereqs.length; i++){
    graph.addPrereq(prereqs[i][1], prereqs[i][0])
  }
  let output = traverse(graph)
  return output.length === numCourses ? output : []
}