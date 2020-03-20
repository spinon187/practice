var generate = function(numRows) {
  let output =[];  
  for(i=0; i<numRows.length;i++){
      let row = [];
        for(j=0;j<i+1;j++){
          if(j==0 || j==i){
            row.push(1)
          }
          else{
            let sum = output[i-1][j-1] + output[i-1][j];
            row.push(sum);
          }
        }
        output.push(row)
      }
  return output;
};



var minScoreTriangulation = function(A) {
  let storage = [];
  let output = 0;  
  for(i=0; i<A.length; i++){
      if(i <= A.length-3){
        storage.push(A[i]*A[i+1]*A[i+2])
      }
      else if(i==A.length-2){
        storage.push(A[i]*A[i+1]*A[0])
      }
      else{
        storage.push(A[i]*A[i+1]*A[0])
      }
    }
  storage.sort((a,b)=>(a-b));
  for(i=0;i<storage.length-2;i++){
    output += storage[i]
  }
  return output;
};
var minScoreTriangulation = function(A) {
  let output = 0;  
  A.sort((a,b)=>(a-b));
  for(i=0;i<A.length-2;i++){
    output += (A[0]*A[1]*A[i+2]);
  }
  return output;
};

var minScoreTriangulation = function(A) {
  let output = 0;  
  A.sort((a,b)=>(a-b));
  for(i=0;i<A.length-2;i++){
    output += (A[0]*A[1]*A[i+2]);
  }
  return output;
};

var minScoreTriangulation = function(A) {
  let total = 0;
  var minHelper = function(A){
    let storage = new Array(A.length);
    let mindex = 1;
    for(i=0; i<A.length; i++){
      if(i <= A.length-3){
        storage[i+1] = (A[i]*A[i+1]*A[i+2]);
        if(storage[i+1] < storage[mindex]){
          mindex = i+1;
        }
      }
      else if(i==A.length-2){
        storage[i+1] = (A[i]*A[i+1]*A[0])
        if(storage[i+1] < storage[mindex]){
          mindex = i+1;
        }
      }
      else{
        storage[0] = (A[i]*A[0]*A[1])
        if(storage[i+1] < storage[mindex]){
          mindex = i+1;
        }
      }


    }
    total += storage[mindex];
    A = A.splice(mindex, 1);
  }
  while(A.length > 2){
    minHelper(A);
  }
  return total
};

var getRow = function(rowIndex) {
    let output = [];   
    for(i=0; i<rowIndex;i++){
        let row = [];
          for(j=0;j<i+1;j++){
            if(j==0 || j==i){
              row.push(1)
            }
            else{
              let sum = output[i-1][j-1] + output[i-1][j];
              row.push(sum);
            }
          
          }
            output.push(row)
        }
    return output[rowIndex];
};

var getRow = function(rowIndex){
  let output = new Array(rowIndex);
  const memo = new Array(Math.ceil(rowIndex/2));
  const fact = x => {
    return x<=1 ? 1 : x*fact(x-1);
  }
  let total = fact(rowIndex);
  let back =
  output[0] = 1;
  if(rowIndex > 0){
    output[rowIndex] = 1;
  }
}