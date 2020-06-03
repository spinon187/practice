const traverse = (node, val1, val2) => {
  let found = 0
  if(node.left){
    results = traverse(node.left, val1, val2);
    if(results[1]) return results
    found += results[0]
  }
  if(node.right){
    results = traverse(node.right, val1, val2);
    if(results[1]) return results
    found += results[0]
  }
  if(node.val === val1 || node.val === val2){
    found += 1
  }
  return [found, found == 2 ? node : null]
}

class TreeNode {
  constructor(val){
    val,
    this.right = null,
    this.left = null
  }
}

// const generateNode = (val, limit) => {
//   const node = new TreeNode(val);
//   if(val+1 < limit) node.left = generateNode(val+1, limit);
//   if(val+2 < limit) node.left = generateNode(val+2, limit);
//   return node;
// }

const generateTree = n => {
  let root = new TreeNode(1), i = 2;
  while(i<n){
    
  }
}