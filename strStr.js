var strStr = function(haystack, needle) {
  if(!needle) return 0;
  for(i=0;i<haystack.length-needle.length;i++){
      if(haystack[i] == needle[0]){
          let checking = true;
          for(j=1;j<needle.length;j++){
            if(haystack[i+j] != needle[j]){
              checking = false;
            }
          if(checking) return i;
          }
      }
  }
  return -1;
};