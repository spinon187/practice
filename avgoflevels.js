var averageOfLevels = function(root) {
  let q = [root], results = [];
  while(q.length){
      let sum = [...q].reduce((x, {val}) => x+val, 0);
      results.push(sum / q.length)
      let nextlevel = [];
      for(i=0;i<q.length;i++){
          if(q[i].left) nextlevel.push(q[i].left)
          if(q[i].right) nextlevel.push(q[i].right)
      }
      q = nextlevel
  }
  return results
};