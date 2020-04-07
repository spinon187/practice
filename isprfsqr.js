
const binS = (s, e, t) => {
  let m = ~~((s+e)/2)
  if(s*s === t || e*e === t || m*m === t){
    return true
  }
  else if(e-s < 2){
    return false
  }
  if(m*m > t){
    return binS(s, m-1, t)
  } else {
    return binS(m+1, e, t)
  }
}


var isPerfectSquare = function(num) {
  return binS(1, ~~(num/2), num)
};