const fill = (arr, cont) => {
  let temp = [], prev = arr[arr.length-1];
  for(let i = 0; i<prev.length; i++){
    if(prev[i].left) temp.push(prev[i].left);
    if(prev[i].right) temp.push(prev[i].right);
    if(temp.length){
      cont = true;
      arr.push(temp)
    }
  }
  // return [arr, cont]
  return cont
}

// const dft = (node, lvl, o) => {
//   if(!node) return;
//   let l = 0, r = 0;
//   if(node.left){
//     l = dft(node.left, lvl+1, o)
//   }
//   if(node.right){
//     r = dft(node.right, lvl+1, o)
//   }
//   if(l-r > 1 || r-l > 1){
//     o = false;
//   }
//   return lvl;
// }

var isBalanced = function(root) {
  if(!root || (!root.left && !root.right)) return true;
  // let output = true;
  // dft(root, 1, output);
  // return output;
  let cont = true, arr = [[root]];
  while(cont){
    // [arr, cont] = fillArr(arr, cont)
    cont = fill(arr, cont)
  }
  for(let i = arr.length-3;i > 1; i--){
    if(arr[i].length < (i+1)*2) return false
  }
};