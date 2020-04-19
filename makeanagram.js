function makeAnagram(a, b) {
  let x = {}, y = {}, count = 0;
  for(let i in a){
    let z = a[i];
    x[z] = x[z]+1 || 1;
  }
  for(let i in b){
    let z = b[i];
    y[z] = y[z]+1 || 1
  }
  Object.keys(x).forEach(k => {
    if(y[k]){
      count += Math.abs(x[k] - y[k]);
      delete x[k];
      delete y[k];
    } else {
      count += x[k]
    }
  })
  Object.values(y).forEach(v => {
    count += v
  })
  return count;
}