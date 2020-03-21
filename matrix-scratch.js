const mrecur = (m, row, col, count) => {
  // count = count || 1;
  count++;
  // console.log(m, row, col, count);
  m[row][col] = 0;
  if(m[row][col+1] && m[row][col+1] === 1){
    count = mrecur(m, row, col+1, count);
  }
  if(m[row][col-1] && m[row][col-1] === 1){
    count = mrecur(m, row, col-1, count);
  }
  if(m[row+1] && m[row+1][col+1] && m[row+1][col+1] === 1){
    count = mrecur(m, row+1, col+1, count);
  }
  if(m[row+1] && m[row+1][col] && m[row+1][col] === 1){
    count = mrecur(m, row+1, col, count);
  }
  if(m[row+1] && m[row+1][col-1] && m[row+1][col-1] === 1){
    count = mrecur(m, row+1, col-1, count);
  }
  return count;
}

const mloop = m => {
  let max = 0;
  for(i=0;i<m.length;i++){
    for(j=0;j<m[i].length;j++){
      if(m[i][j] === 1){
        max = Math.max(max, mrecur(m, i, j, 0))
      }
    }
  }
  console.log(max);
}


let zoop = [
  [0, 0, 0, 1, 0],
  [0, 0, 1, 1, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0]
];

mloop(zoop)