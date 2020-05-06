var convert = function(s, numRows) {
  if(numRows === 1) return s;
  let arrs = [];
  for(let i = 0; i<numRows; i++){
    arrs.push('')
  }
  let counter = 0, up = true, down = false;
  for(let i = 0; i<s.length; i++){
    arrs[counter] += s[i];
    if(counter === 0){
      up = true;
      down = false;
    }
    if(counter === numRows-1){
      up = false;
      down = true;
    }
    if(up) counter++;
    if(down) counter--;
  }
  let op = '';
  for(let i = 0; i<numRows; i++){
    op += arrs[i]
  }
  return op
};