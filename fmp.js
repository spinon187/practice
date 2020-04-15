const swap = (arr, i) => {
  let swapped = false, one = arr[i], two = arr[one-1];
  if(one !== two){
    arr[i] = two;
    arr[one-1] = one;
    swapped = true
  }
  if(swapped && arr[i] && arr[i] < arr.length) swap(arr, i)
}

var firstMissingPositive = function(nums) {
  let j = 0;
  for(let i in nums){
    if(nums[i] && nums[i] < nums.length) swap(nums, i);
    while(nums[j] === j+1){
      j++;
    }
  }
  return j+1;
};