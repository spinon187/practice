const dig = (node, depth, max) => {
  if(!node) return;
  if(node) depth = depth+1;
  max = Math.max(depth, max);
  if(node.left){
      max = dig(node.left, depth, max)
  }
  if(node.right){
      max = dig(node.right, depth, max)
  }
  return max
}

var maxDepth = function(root) {
  return dig(root, 0, 0) || 0
};