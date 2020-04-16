var NumArray = function(nums) {
  this.arr = nums 
};

NumArray.prototype.sumRange = function(i, j) {
  let op = 0;
  for(i; i<=j; i++){
    op += this.arr[i]
  }
  return op
};