// function minimumBribes(q) {
//   q.unshift(0)
//   let i = 0, count = 0, max=0;
//   for(i;i<q.length;i++){
//     if(q[i])
//     if(q[i] > i + 2){
//       count = 'Too chaotic';
//       i=q.length;
//     }
//     else{
//       if(q[i]<i){
//       for(let j=0;j<i;j++){
//         if(q[j] > q[i]) count++
//       }
//       }
//     }
//   }
//   console.log(count)
// }

const minimumBribes = q => {
  q.unshift(0);
  let count = 0;
  for(let i = q.length-1; i>0; i--){
    if(q[i]-i > 2) return console.log('Too chaotic');
    if(q[i] < i){
      count += i-q[i]
    } else {
      if(q[i-1] && q[i-1]>q[i]) count++;
      if(q[i-2] && q[i-2]>q[i]) count++;
    }
    // if(q[i]>i){
    //   missing.add(i);
    // } else if(missing.has(q[i])){
    //   missing.delete(q[i])
    // }
    // count += missing.size
  }
  console.log(count)
}

const minimumBribes = q => {
  let max = 0, count = 0;
  for(let i in q){
    if(q[i] > max+2) return console.log('Too chaotic');
    if(q[i] < max){
      count += max-q[i]
    }
    max = q[i]
  }
  console.log(count)
}