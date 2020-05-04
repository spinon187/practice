const bfsInvert = node => {
  if(!node) return;
  [node.left, node.right] = [node.right, node.left];
  bfsInvert(node.right);
  bfsInvert(node.left);
}

var invertTree = function(root) {
  bfsInvert(root);
  return root;
};