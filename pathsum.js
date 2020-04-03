const dfs = (node, t, sum, val) => {
  if(!node) return;
  sum += node.val;
  if(!node.left && !node.right){
    if (sum === t) val = true;
  }
  if(node.left && !val){
    val = dfs(node.left, t, sum, val)
  }
  if(node.right && !val){
    val = dfs(node.right, t, sum, val)
  }
  return val;
}

var hasPathSum = function(root, sum) {
  let output;
  output = dfs(root, sum, 0, false);
  return output ? true : false;
};