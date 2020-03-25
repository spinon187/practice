var removeDuplicates = function(nums) {
  // let len = 1, back = nums.length;
  // for(i=1;i<back;i++){
  //   if(nums[i] == nums[i-1]){
  //     nums.push(nums.splice(i, 1));
  //     back--;
  //       i--;
  //   } else {
  //       len++;
  //   }
  // }
  // return len
    let j = 0;
    for(i=1;i<nums.length;i++){
        if(nums[i] !== nums[j]){
            j++;
            nums[j] = nums[i]
        }
    }
    return j+1;
};