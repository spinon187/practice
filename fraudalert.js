const getMedian = q => {
  let med = ~~(s.length/2);
  return s.length % 2 > 0 ? s[med] : (q[med]+q[med+1])/2
}

const activityNotifications = (ex, d) => {
  let q = [], count = 0, initSort = false;
  for(let i in ex){
    if(q.length < d){
      q.push(ex[i])
    } else if(q.length === d){
      if(!initSort){
        q.sort((a,b) => a-b)
      }
      let m = getMedian(q);
      if(ex[i] >= m*2) count++
      q.splice(q.indexOf(q[i-d]), 1, q[i]).sort((a,b) => a-b)
    }
  }
  return count
}

// const getMedian = (a, v, prev) => {

// }

const gm = (a, d) => {
  let mI = ~~(d/2), j = 0, mC = 0;
  while(mC<mI){
    j++;
    if(a[j] > 0){
      mC += a[j]
    }
  }
  if(d%2<1&&mI===mC){
    let first = j;
    j++;
    while(a[j] === 0){
      j++;
    }
    return (first+j)/2
  } else {
    return j
  }
}


const activityNotifications = (ex, d) => {
  let vals = new Array(201), i = 0, count = 0;
  for(i;i<d-1;i++){
    vals[ex[i]]++
  }
  let m = gm(vals, d);
  for(i;i<ex.length;i++){
    if(m*2 <= ex[i]) count++;
    vals[ex[i-d]]--;
    vals[ex[i]]++;
    m = gm(vals, d)
  }
  return count
}