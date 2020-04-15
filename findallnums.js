var findDisappearedNumbers = function(nums) {
  // let k = new Set([...nums]), output = [], max = nums.length;
  // for(let i = 1;i<=max;i++){
  //   if(!k.has(i)) output.push(i);
  //   if(i>max) max = i;
  // }
  // return output
  let op = [];
  for(let i = 1;i<=nums.length;i++){
    nums[nums[i]-1] = 0
  }
  for(let i = 0;i<nums.length;i++){
    if(nums[i] > 0) op.push(nums[i])
  }
  return op
};