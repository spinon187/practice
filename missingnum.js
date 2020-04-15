var missingNumber = function(nums) {
  let k = new Set([...nums]), i = 0;
  for(i; i<nums.length;i++){
      if(!k.has(i)){
          return i
      }
  }
  return i
};