var isPalindrome = function(x) {
  if(x < 0) return false;
  // let split = [];
  let a = x, b = 0;
  while(a > 0){
      let y = z%10;
      z = (z-y)/10;
      b = (b*10)+y;
  }
  // let j = split.length-1, good = true, i=0;
  // while(i<j && good){
  //   if(split[i] !== split[j]) good = false;
  //   i++;
  //   j--;
  // }
  return x===b;
};