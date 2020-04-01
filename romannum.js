var romanToInt = function(s) {
  const d = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000
  }
  let total = 0;
  for(i=0;i<s.length;i++){
    if(d[s[i]] < d[s[i+1]] || d[s[i]] < d[s[i+2]]){
      total -= d[s[i]]
    } else {
      total += d[s[i]]
    }
  }
  return total;
};