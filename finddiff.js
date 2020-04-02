var findTheDifference = function(s, t) {
  // s = s.split('').sort();
  // t = t.split('').sort();
  // for(let i in t){
  //     if(!s[i] || s[i] !== t[i]) return t[i];
  // }
  let d = {};
  for(let i in t){
    if(s[i]) d[s[i]] = d[s[i]] ? d[s[i]]+1 : 1;
  }
  for(let j in t){
    if(!d[t[j]]){
      return t[j]
    } else {
      d[t[j]]--;
      if(d[t[j]] < 0) return t[j]
    }
  }

};