const traverse = (node, val1, val2) => {
  if(node.val === val1 || node.val === val2) return true;
  const left = traverse(node.left, val1, val2),
  right = traverse(node.right, val1, val2);
  return (left && right) ? node : left || right;
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