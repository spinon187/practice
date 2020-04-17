// const getIndex = (n, r) => {
//   if(n === 1) return 0;
//   let count = 1;
//   while(n > r){
//     n /= r;
//     count ++;
//   }
//   return count;
// }

// const countTriplets = (arr, r) => {
//   let vals = [0], k = {};
//   for(let i = 1; i<arr.length; i++){
//     // if(k[arr[i]]){
//     //   vals[k[arr[i]]]++;
//     // } else {
//     //   let tar = getIndex(arr[i]);
//     //   k[arr[i]] = tar;
//     //   // while(vals.length-2 < tar){
//     //   //   vals.push(0)
//     //   // }
//     //   // vals.push(1)
//     //   vals[tar] = 1;
//     // }
//     if(!k[arr[i]]){
//       let tar = getIndex(arr[i]);
//       k[arr[i]] = tar;
//       while(arr.length-1 < tar){
//         arr.push(0)
//       }
//     }
//     vals[k[arr[i]]]++

//   }
//   let counts = 0;
//   for(let x = 0; x<vals.length-2; x++){
//     counts += (vals[x]*vals[x+1]*vals[x+2])
//   }
//   return counts;
// }

const getIndex = (n, r) => {
  if(n === 1) return 0;
  let count = 1;
  while(n > r && count > 0){
    n /= r;
    if(n%r<1){
      count ++;
    } else {
      count = -1
    }
  }
  return count;
}

const countTriplets = (arr, r) => {
  arr.sort((a,b) => (a-b));
  let vals = [0], j = 0;
  for(let i = 0; i<arr.length; i++){
    if(arr[i] === 1){
      vals[0]++
    } else (arr[i] % r === 0){
      if(arr[i] === arr[i-1]){
        vals[j]++;
      } else if(arr[i] / r === arr[i-1]){
        j++;
        vals.push(1)
      } else {
        j += 2;
        vals.push(0)
      }
    }
  }
  let counts = 0;
  for(let x = 0; x<vals.length-2; x++){
    counts += (vals[x]*vals[x+1]*vals[x+2])
  }
  return counts;
}

const countTriplets = (arr, r) => {
  let k = {0: 0}, fail = new Set();
  for(let i in arr){
    let x = arr[i];
    if(k[x]){
      k[x]++;
    } else if(x%r===1 && !fail.has(x)){
      let tar = getIndex(x, r);
      if(tar > -1){
        k[tar] = 1;
      } else {
        fail.add(x)
      }
    }
  }
  let count = 0, vals = Object.keys(k);
  vals.forEach(v => {
    if(k[v+1] && k[v+2]){
      count += (k[v]*k[v+1]*k[v+2])
    }
  })
  return count
}