var firstUniqChar = function(s) {
  let good = {}, bad = {}, q = [];
  for(i=s.length-1;i>=0;i--){
      if(good[s[i]]) {
          delete good[s[i]]
          bad[s[i]] = true;
          while(bad[q[q.length-1]]){
              q.pop()
          }
      } else if(!bad[s[i]]){
          good[s[i]] = i;
          q.push(s[i])
      }
  }
  let output = good[q[q.length-1]];
  return q.length ? output : -1
};