var reconstructQueue = function(people) {
  output = [];
  people.sort((a,b) => a[0] === b[0] ? a[1] - b[1] : b[0] - a[0]);
  people.forEach(val => output.splice(val[1], 0, val));
  return output;
};

var queryString = function(S, N) {
  S = S.split('');
  let out = 0;
  let mult = 1;
  for(i=S.length-1;i>=0;i--){
    out = out + (mult * parseInt(S[i]));
    mult = mult*2;
  }
  if(out == N){
    return true
  }
  else{
    return false
  }
};

var queryString = function(S, N) {
  let bin = N.toString(2);
  return S.includes(bin);
};

var longestCommonSubsequence = function(text1, text2) {
  let len = 0;
  text1 = text1.split('');
  text2 = text2.split('');
  text1.length > text2.length ? (short = text2, long = text1) : (short = text1, long = text2);
  // for(i=0; i<short.length; i++){
  //   if(!long.includes(short[i])){
  //     short.splice(i, 1);
  //     i--;
  //   }
  // }
  // for(i=0; i<long.length; i++){
  //   if(!short.includes(long[i])){
  //     long.splice(i, 1);
  //     i--;
  //   }
  // }
  // for(i=0;i<long.length;i++){
  //   if(short[i] !== long[i]){
  //     long.splice(i, 1);
  //     i--;
  //   }
  // }
  // if(short == long){
  //   return short.length;
  // }
  
};