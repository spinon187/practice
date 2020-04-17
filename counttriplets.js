const getCount = (k, c, r) => {
  let b = c/r, a = b/r, count = 0;
  if(k[a] && k[b]){
    if(k[a][k[a].length-1] < k[b][0]){
      count += (k[a].length*k[b].length)
    } else {
      for(let i in k[b]){
        let x = k[a].length-1, toAdd = k[a].length;
        while(k[a][x] > k[b][i] && x>=0){
          x--;
          toAdd--;
        }
        count += toAdd;
      }
    }
  }
  return count;
}


const countTriplets = (arr, r) => {
  let k = {}, count = 0;
  for(let i in arr){
    let x = arr[i];
    if(!k[x]){
      k[x] = [i]
    } else {
      k[x].push(i)
    }
    count += getCount(k, arr[i], r)
  }
  console.log(Object.entries(k))
  return count
}