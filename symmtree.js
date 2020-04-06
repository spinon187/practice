const pushRow = (arr, x) => {
  let tempArr = arr.slice(arr.length-x), cont = false;
  tempArr.forEach(node => {
      if(!node){
          arr.push(null)
          arr.push(null)
      } else {
          arr.push(node ? node.left : null);
          arr.push(node ? node.right : null);
          if(node.left && !cont){
              if(node.left.left || node.left.right) {
                  cont = true
              }
          }
          if(node.right && !cont){
              if(node.right.left || node.right.right){
                  cont = true
              }
          }
      }
  })
  return [arr, cont];
}

const checkBack = (arr, x, val) => {
  let tempArr = arr.splice(arr.length-x), i = 0, j = tempArr.length-1;
  while(i<j && val){
      if(tempArr[i] && tempArr[j]){
          if(tempArr[i].val !== tempArr[j].val){
             val = false;
          } 
      } else if((!tempArr[i] && tempArr[j]) || !tempArr[j] && tempArr[i]){
          console.log(i, j)
          val = false
      }
      i++;
      j--;
  }
  return [arr, val]
}

var isSymmetric = function(root) {
  if(!root) return true;
  let q = [root], x = 1, output = true, cont = true;
  while(cont){
      [q, cont] = pushRow(q, x);
      x = x * 2;
  }
  while(output && x>1){
      [q, output] = checkBack(q, x, output);
      x = x/2
  }
  return output;
};