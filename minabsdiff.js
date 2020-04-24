function minimumAbsoluteDifference(arr) {
  let min = null;
  arr.sort((a,b)=>a-b)
  for(let i=0; i<arr.length-1; i++){
    min = min === null ? Math.abs(arr[i+1]-arr[i]) : Math.min(min, Math.abs(arr[i+1]-arr[i]))
  }
  return min
}