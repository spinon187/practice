const bloop = (arr, start, end, val, max) => {
  for(let i = start-1; i<end; i++){
    arr[i] += val;
    max = Math.max(max, arr[i])
  }
  return max;
}

function arrayManipulation(n, queries) {
  let diff = new Array(n).fill(0), max = 0;
  for(let i in queries){
    max = bloop(diff, queries[i][0], queries[i][1], queries[i][2], max)
  }
  return max
}
