const swap = (arr, i, count) => {
  count = 0;
  if(arr[i] < arr[i-1]){
    [arr[i], arr[i-1]] = [arr[i-1], arr[i]];
    count++;
    count += swap(arr, i-1, count);
  }
  return count;
}

const minimumBribes = q => {
  let count = 0;
  for(let i = 0; i<q.length; i++){
    if(q[i] > i+3) return console.log('Too chaotic');
    count += swap(q, i, count);
  }
  console.log(count);
}