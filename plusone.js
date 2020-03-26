var lengthOfLastWord = function(s) {
  if(!s) return 0;
  let spaced = true, count = 0;
  for(i=0; i<s.length; i++){
    if(s[i] == ' '){
        spaced = true;
    } else {
        if(spaced) count = 0;
        count++;
        spaced = false;
    }
  }
  return count;
};