var isPowerOfTwo = function(n) {
  if(n<1) return false;
  let output = true;
  while(output && n > 2){
      n /= 2;
      if(n%2 > 0) output = false
  }
  return output
};