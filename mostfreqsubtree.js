const dfs = (node, k) => {
  if(!node) return;
  let sum = node.val;
  if(node.left) sum += dfs(node.left, k);
  if(node.right) sum += dfs(node.right, k);
  k[sum] = k[sum]+1 || 1;
  return sum;
}

var findFrequentTreeSum = function(root) {
  let max = [], k = {};
  dfs(root, k);
  Object.keys(k).forEach(val => {
    if(!max.length || k[val] > k[max[0]]){
      max = [val];
    } else if(k[max[0]] === k[val]){
      max.push(val)
    }
  })
  return max;
};