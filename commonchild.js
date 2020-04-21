const commonChild = (s1, s2) => {
  s1 = s1.split(''), s2 = s2.split('');
  let d1 = {}, d2 = {}, k1 = new Set([...s1]), k2 = new Set([...s1]);
  for(let i in s1){
    if(k2.has(s1[i])){
      d1[s1[i]] = d1[s1[i]] ? [...d1[s1[i]], i] : [i]
    }
  }
  for(let i in s2){
    if(k1.has(s2[i])){
      d2[s2[i]] = d2[s2[i]] ? [...d2[s2[i]], i] : [i]
    }
  }
  
};