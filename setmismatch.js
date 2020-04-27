
var findErrorNums = function(nums) {
  nums.sort((a,b)=>a-b);
  let d, m, i=0;
  for(i;i<nums.length;i++){
    if(d && m){
      return [d, m]
    }
    if(nums[0] > 1){
      m = 1
    }
    if(nums[i] === nums[i+1]){
      d = nums[i]
    }
    if(nums[i+1] > nums[i]+1){
      m = nums[i]+1
    }
  }
  if(!m) m = i;
  return [d, m]
};