var preorderTraversal = function(root) {
  let stack = [], results = [];
  while(root || stack.length){
      if(root){
          results.push(root.val)
          stack.push(root.right, root.left)
      }
      root = stack.pop()
  }
  return results
};