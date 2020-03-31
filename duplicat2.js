var containsNearbyDuplicate = function(nums, k) {
    if(k===0) return false;  
    if(nums.length < k-1){
      let comp = new Set([...nums]);
      return comp.size < nums.length
    }

  let back = new Set(nums.slice(0, k)), front = new Set(nums.slice(k+1, k+k+1));
  if(k > back.size || k > front.size) {
    return true;
  }
  console.log(back, front, nums[k])
  for(i=k;i<nums.length;i++){
    if(i !== k){
      back.delete(nums[i-k-1])
      back.add(nums[i-1])
      front.delete(nums[i]);
      if(nums[i+k]) front.add(nums[i+k])
    }
    if(back.has(nums[i]) || front.has(nums[i])) return true
  }
  return false
};