var missingNumber = function(nums) {
  // let k = new Set([...nums]), i = 0;
  // for(i; i<nums.length;i++){
  //     if(!k.has(i)){
  //         return i
  //     }
  // }
  // return i
  let j = 0;
  for(let i in nums){
    [nums[i], nums[nums[i]]] = [nums[nums[i]], nums[i]];
    while(nums[j] === j){
      j++
    }
  }
  return j;
};