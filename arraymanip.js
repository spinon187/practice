const bloop = (arr, start, end, val, max) => {
  for(let i = start-1; i<end; i++){
    arr[i] += val;
    max = Math.max(max, arr[i])
  }
  return max;
}

function arrayManipulation(n, queries) {
  let diff = [];
  for(let j = 0; j<=n; j++){
    if(j>=queries[0][0]-1 && j<queries[0][1]){
      j.push(queries[0][2])
    } else {
      j.push(0)
    }
  }
  for(let i = 1; i<queries.length; i++){
    max = bloop(diff, queries[i][0], queries[i][1], queries[i][2], max)
  }
  return max
}


const badLoop = (arr, i, k, max, cont) => {
  let base = [arr[i][0], arr[i][1]], val = arr[i][2];
  cont = false;
  for(i=i+1; i<arr.length; i++){
    let check = [Math.max(base[0], arr[i][0]), Math.min(base[1], arr[i][1]), val+arr[i][1]];
    if(check[0]<=check[1]){
      k.push(check);
      max = Math.max(max, check[2]);
      cont = true;
    }
  }
  return [k, max, cont];
}

const arrayManipulation = (n, queries) => {
  let max = 0, cont = true, prev = queries;
  while(cont){
    let k = [];
    for(let i in prev){
      [k, max, cont] = badLoop(prev, i, k, max, cont);
    }
    prev = k;
  }
  console.log(max)
}
