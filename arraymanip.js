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
      j.push(queries[0][3])
    } else {
      j.push(0)
    }
  }
  for(let i = 1; i<queries.length; i++){
    max = bloop(diff, queries[i][0], queries[i][1], queries[i][2], max)
  }
  return max
}

// const arrayManipulation = (n, queries) => {
//   let k = {};
//   for(let i = 0; i<queries.length; i++){

//   }
// }
