var maxAncestorDiff = function(root) {
  let max = 0;
  const traverse = (node, high, low) => {
      if(!node){
          return max
      }
      let r, l, anc1, anc2, rdiff, ldiff;
      if(high > node.val){
          anc1 = high;
      }
      else{
          anc1 = node.val
      }
        if(low < node.val){
          anc2 = low;
      }
      else{
          anc2 = node.val
      }
      if(node.right){
        r = node.right.val;
      }
      if(node.left){
        l = node.left.val;
      }
      if(Math.abs(anc1 - r) > Math.abs(anc2-r)){
          rdiff = Math.abs(anc1 - r)
      }
      else{
          rdiff = Math.abs(anc2 - r)
      }
      if(Math.abs(anc1 - l) > Math.abs(anc2-l)){
          ldiff = Math.abs(anc1 - l)
      }
      else{
          ldiff = Math.abs(anc2 - l)
      }
      
      if(rdiff > max){
        max = rdiff;
      }
      if(ldiff > max){
        max = ldiff;
      }
      if(node.right){
          if(node.right.right || node.right.left){
              traverse(node.right, anc1, anc2)
          }
          
      }
      if(node.left){
        if(node.left.left || node.left.right){
                traverse(node.left, anc1, anc2)
        }

    }
  }
  traverse(root, root.val, root.val);
  return max;
};