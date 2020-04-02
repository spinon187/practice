var moveZeroes = function(nums) {
  let j = 0;
  for(let i in nums){
      while(j<i && nums[j] !== 0){
          j++
      }
      if(nums[i] !== 0 && nums[j] === 0){
          [nums[i], nums[j]] = [nums[j], nums[i]]
      }
  }
};