const fillArr = (tracker, cont) => {
  let prev = tracker[tracker.length-1], next = [];
  cont = false;
  for(let i in prev){
    if(prev[i].left){
      next.push(prev[i].left);
      if(prev[i].left.left || prev[i].left.right) cont = true;
    }
    if(prev[i].right){
      next.push(prev[i].right);
      if(prev[i].right.left || prev[i].right.right) cont = true;
    }
  }
  if(next.length) tracker.push(next);
  return [tracker, cont];
}

var levelOrder = function(root) {
  if(!root){
      return []
  } else {
    let tracker = [[root]], cont = true;
    while(cont){
      [tracker, cont] = fillArr(tracker, cont)
    }
    return tracker.map(sub => sub.map(node => node.val))
  }
};