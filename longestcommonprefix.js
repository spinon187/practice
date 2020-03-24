var longestCommonPrefix = function(strs) {
  if(!strs.length) return '';
  let output = '', base = strs[0].split(''), matched = true;
  for(i=0;i<base.length;i++){
      if(matched){
          let letter = base[i];
          for(j=1;j<strs.length;j++){
              if(strs[j].charAt(i) != letter){
                  matched = false;
          }
      }
      if(matched) output += letter;
      }
  }
  return output;
};