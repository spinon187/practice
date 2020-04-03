const dfs = (node, t, sum, list, final) => {
  if(!node) return;
  sum += node.val;
  if(!node.left && !node.right){
    if (sum === t){
      final.push([...list, node.val]);
    } ;
  }
  if(node.left){
    final = dfs(node.left, t, sum, [...list, node.val], final)
  }
  if(node.right){
    final = dfs(node.right, t, sum, [...list, node.val], final)
  }
  return final;
}

var pathSum = function(root, sum) {
  if(!root) return [];
  return dfs(root, sum, 0, [], []);
};