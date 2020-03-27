const uniqueSort = arr => {
  let d = new Set(), r = [];
  for(let i = 0; i<arr.length; i++){
    if(!d.has(arr[i])){
      if(!r.length){
        r.push(arr[i])
      } else {
        let x = arr[i]
        for(let j = 1; j<=r.length; j++){
          if(!r[j]){
            r.push(x)
          } else {
            if(r[j] > x){
              [x, r[j]] = [r[j], x]
            }
          }
        }
      }      
    }
  }
  return r;
}

findB = (arr, b, s, e) => {
  let res;
  while(!res){
    if(b === arr[s]){
      res = s
    } else if(b === arr[e]){
      res = s
    } else if(arr[s] > b){
        res = s;
    } else if(arr[e] < b){
        res = e
    }
    let m = ~~((s+e)/2);
    if(b === arr[m]){
      res = m;
    } else if(b > arr[m]){
      res = findB(arr, b, m, e)
    } else if(b < arr[m]){
      res = findB(arr, b, s, m)
    }
  }
  return res;
}

function triplets(a, b, c) {
  a = uniqueSort(a);
  b = uniqueSort(b);
  c = uniqueSort(c);
  let count = 0;
  for(let i = 0; i<b.length; i++){
    // let aC = 0, cC = 0;
    // while(a[aC] <= b[i]){
    //   aC++
    // }
    // while(c[cC] <= b[i]){
    //   cC++
    // }
    // count += (aC*cC)
  }

  return count;
}