const addNodes = (node, dict) => {
  if(!node) return null;
  if(!dict.has(node)){
    let newNode = new Node(node.val);
    dict.set(node, newNode);
    node.neighbors.forEach(n => {
      newNode.neighbors.push(addNodes(n, dict))
    })
    return newNode
  } else {
    return dict.get(node)
  }
}

var cloneGraph = function(node) {
  let k = new WeakMap();
  return addNodes(node, k)
};