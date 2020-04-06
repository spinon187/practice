const dig = (node, depth, min) => {
  if(!node) return;
  if(node) depth = depth+1;
  if(!node.left && !node.right){
      min = !min ? depth : Math.min(min, depth)
  }
  if(node.left){
      min = dig(node.left, depth, min)
  }
  if(node.right){
      min = dig(node.right, depth, min)
  }
  return min
}

var minDepth = function(root) {
  return dig(root, 0, null) || 0
};