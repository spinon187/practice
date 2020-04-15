const clearOut = (arr, row, col) => {
  arr[row][col] = '0';
  if(col > 0){
    if(arr[row][col-1] === '1') clearOut(arr, row, col-1);
  };
  if(col < arr[row].length-1){
    if(arr[row][col+1] === '1') clearOut(arr, row, col+1);
  };
  if(row > 0){
    if(arr[row-1][col] === '1') clearOut(arr, row-1, col);
  };
  if(row < arr.length-1){
    if(arr[row+1][col] === '1') clearOut(arr, row+1, col)
  }
}

var numIslands = function(grid) {
  let count = 0;
  for(let i = 0; i<grid.length; i++){
    for(j = 0; j<grid[i].length; j++){
      if(grid[i][j] === '1'){
        count++;
        clearOut(grid, i, j)
      }
    }
  }
  return count
};