var smallerNumbersThanCurrent = function(nums) {
  let sorted = [...nums].sort((a,b)=>a-b), k = {}, op = [];
  for(let i = 0; i<sorted.length; i++){
    if(!k.hasOwnProperty([sorted[i]])) k[sorted[i]] = i; 
  }
  for(let i = 0; i<nums.length; i++){
    op.push(k[nums[i]])
  }
  return op
};