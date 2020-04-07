var rob = function(nums) {
  if(nums.length < 2) return nums[0] || 0;  
  let rt = [nums[0], Math.max(nums[0], nums[1])];
  for(let i = 1; i<nums.length; i++){
    rt[i] = Math.max(rt[i-1], rt[i-2] + nums[i])
  }
  return rt[rt.length-1]
};