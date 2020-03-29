var generate = function(numRows) {
  let output = [];
  if(numRows > 0) output.push([1]);
  if(numRows > 2) output.push([1, 1])
  for(i=2;i<=numRows;i++){
    output.push(new Array(i+1));
    output[i][0] = 1;
    output[i][output[i].length-1] = 1;
    for(j=1;j<output[i].length-1;j++){
      output[i][j] = output[i-1][j] + output[i-1][j-1]
    }
  }
  return output
};