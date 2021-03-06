var dominantIndex = function(nums) {
  let max = [nums[0], 0], second = null;
  for(let i = 1; i<nums.length; i++){
    if(nums[i] > max[0]){
      second = max[0];
      max = [nums[i], i];
    } else if(!second || nums[i] > second) {
      second = nums[i]
    }
  }
  if(max[0] > second*2){
    return max[1]
  } else {
    return -1
  }
};

const dominantIndex = nums => {
  let n = [...nums].sort((a,b)=>(b-a));
  return n[0] >= n[1] ? nums.indexOf(n[0]) : -1
}