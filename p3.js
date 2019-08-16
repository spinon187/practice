var largestValues = function(root) {
  let rows = []; 
  const traverse = (node, row) => {
    if(!node){
      return rows
    }

    if(node){
      if(!rows[row]){
        rows[row] = node.val;
      }
      else if(rows[row] < node.val){
        rows[row] = node.val;
      }
    }
    if(node.right !== null){
      traverse(node.right, row+1)
    }
    if(node.left !== null){
      traverse(node.left, row+1)
    }
  }
  traverse(root, 0);
  return rows;
};

var countSubstrings = function(s) {
  let count = 0;
  let dic = {};
  for(i=0;i<s.length;i++){
      if(!dic.hasOwnProperty(s[i])){
          dic[s[i]] = 1;
      }
      else{
        dic[s[i]]++;
      }
      count += dic[s[i]];
  }
  return count;
};

"fdsklf"