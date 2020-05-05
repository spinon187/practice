var findShortestSubArray = function(nums) {
  let k = {}, max = 0, min = null;
  for(let i = 0; i<nums.length; i++){
    let num = nums[i];
    if(!k[num]) k[num] = [];
    k[num].push(i);
    max = Math.max(max, k[num].length);
  }
  let arr = Object.values(k);
  for(let i = 0; i<arr.length; i++){
    if(arr[i].length === max){
        let a = arr[i]
      min = min === null ? a[a.length-1]-a[0] + 1 : Math.min(a[a.length-1]-a[0]+1, min)
    }
  }
  return min
};