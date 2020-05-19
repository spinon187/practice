var findRedundantConnection = function(edges) {
  let op = [], connected = new Set();
  for(let i = 0; i< edges.length; i++){
    let first = edges[i][0], second = edges[i][1];
    if(connected.has(first) && connected.has(second)){
      op = [first, second]
    }
    if(!connected.has(first)){
      connected.add(first)
    }
    if(!connected.has(second)){
      connected.add(second)
    }
  }
  return op
};