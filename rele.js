var removeElement = function(nums, val) {
  let j = 0;
  for(i=0;i<nums.length;i++){
    if(nums[i] !== val){
      nums[j] = nums[i];
      j++;
    }
  }
  return j+1;
};