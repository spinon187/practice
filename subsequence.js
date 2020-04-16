var isSubsequence = function(s, t) {
  let j = 0;
  for(let i in t){
    if(t[i] === s[j]){
      j++;
    }
  }
  return j === s.length+1 ? true : false;
};