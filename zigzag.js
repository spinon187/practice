var convert = function(s, numRows) {
  let arrs = [];
  for(let i = 0; i<numRows; i++){
    arrs.push([])
  }
  let counter = -1, up = true, down = false;
  for(let i = 0; i<s.length; i++){
    if(counter < 0){
      up = true;
      down = false;
    } 
    if(up) counter++;
    if(counter === numRows){
      up = false;
      down = true;
    }
    if(down) counter--;
    arrs[i].push(s[i]);
  }
  let op = '';
  for(let i = 0; i<numRows; i++){
    op += arrs[i].join('')
  }
  return op
};