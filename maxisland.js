const crawl = (arr, row, col, area) => {
  area = 1;
  arr[row][col] = 0;
  if(col > 0){
    if(arr[row][col-1]) area += crawl(arr, row, col-1, area);
  };
  if(col < arr[row].length-1){
    if(arr[row][col+1]) area += crawl(arr, row, col+1, area);
  };
  if(row > 0){
    if(arr[row-1][col]) area += crawl(arr, row-1, col, area);
  };
  if(row < arr.length-1){
    if(arr[row+1][col]) area += crawl(arr, row+1, col, area)
  }
  return area;
}

var maxAreaOfIsland = function(grid) {
  let max = 0;
  for(let i = 0; i<grid.length; i++){
    for(let j = 0;j<grid[i].length; j++){
      if(grid[i][j]){
        max = Math.max(max, crawl(grid, i, j, 0))
      }
    }
  }
  return max;
};