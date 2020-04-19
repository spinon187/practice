function isValid(s) {
  let k = {};
  for(let i in s){
    let x = s[i];
    k[x] = k[x]+1 || 1;
  }
  let comp = {};
  Object.values(k).forEach(v => {
    comp[v] = comp[v]+1 || 1
  })
  console.log(comp)
  let arr = Object.keys(comp).sort((a,b)=>(a-b));
  console.log(arr)
  if(arr.length > 2) return 'NO';
  if(arr.length === 1) return 'YES';
  if(arr[1]-arr[0] > 1){
    if((arr[0] == 1 && comp[arr[0]] === 1) || (arr[1] == 1 && comp[arr[1]] === 1)){
      return 'YES'
    } else {
      return 'NO'
    }
  }
  if(comp[arr[0]] === 1 || comp[arr[1]] === 1){
    return 'YES'
  } else {
    return 'NO'
  }
}