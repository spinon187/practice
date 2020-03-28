var rotate = function(nums, k) {
  let oF = nums.slice(nums.length-k), j=0;
  for(let i in nums){
      if(j===oF.length) j = 0;
      [oF[j], nums[i]] = [nums[i], oF[j]];
      j++
  }
};