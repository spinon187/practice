var singleNumber = function(nums) {
  let good = new Set(), bad = new Set();
  for(i=0;i<nums.length;i++){
    if(!bad.has(nums[i])){
      if(!good.has(nums[i])){
        good.add(nums[i])
      } else {
        good.delete(nums[i]);
        bad.add(nums[i])
      }
    }
  }
  return good.values().next().value;
};