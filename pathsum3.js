const dfs = (node, t, sum, count, trail) => {
  if(!node) return;
  let tr = [...trail, node.val], i = tr.length, ;
  while(i>=0)
  if(sum + node.val === t) count++;
  if(node.left){
      count = dfs(node.left, t, sum+node.val, count)
  }
  if(node.right){
      count = dfs(node.right, t, sum+node.val, count)
  }
  return count;
}
var pathSum = function(root, sum) {
// if(!root) return 0;
  return dfs(root, sum, 0, 0)
};