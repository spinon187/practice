function luckBalance(k, contests) {
  let l = [], total = 0;
  for(let i in contests){
    if(contests[i][1] === 0){
      total += contests[i][0]
    } else {
      let val = contests[i][0];
      l.sort((a,b)=>(b-a));
      if(l.length < k){
        l.push(val);
        total += val
      } else {
        if(l[l.length-1] < val){
          total -= 2*l.pop();
          l.push(val);
          total += val;
        } else {
          total -= val;
        }
      }
    }
  }
  return total
}