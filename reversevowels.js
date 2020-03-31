var reverseVowels = function(s) {
  s = s.split('')
  let v = new Set(['a','e','i','o','u','A','E','I','O','U']), i = 0, j = s.length-1;
  while(i<j){
      if(v.has(s[i])){
          let x = true;
          while(i<j && x){
              if(v.has(s[j])){
                  [s[i], s[j]] = [s[j], s[i]];
                  x = false;
              }
              j--
          }
      }
      i++
  }
  return s.join('');
};