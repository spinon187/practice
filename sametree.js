var isSameTree = function(p, q) {
    if((!p && q) || (!q && p)) return false;
    if(!p && !q) return true;
    let stack = [[p,q]], output = true;
    while(stack.length && output){
      let x = stack.pop();
      if(x.val[0] !== x.val[1]){
        output = false;
      }
      if(x[0].left){
        if(x[1].left){
          stack.push([x[0].left, x[1].left])
        } else {
          output = false;
        }
      } else if(x[1].left && !x[0].left) {
        output = false;
      }
      if(x[0].right){
        if(x[1].right){
          stack.push([x[0].right, x[1].right])
        } else {
          output = false;
        }
      } else if(x[1].right && !x[0].right) {
        output = false;
      }
    }
    return output;
};