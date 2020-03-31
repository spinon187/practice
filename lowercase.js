var toLowerCase = function(str) {
  str = str.split('');
  str2 = '';
  for(i=0;i<str.length;i++){
      str2 += str[i].toLowerCase();
  }
  return str2
};