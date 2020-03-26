const binsrch = (arr, t, start, end) => {
  if(start == end){
    if(arr[start] >= t){
        return start
    } else {
        return start+1
    }
  } else if (start+1 == end){
      if(arr[start] == t){
          return start
      } else if(arr[end] == t){
          return end
      } else if(arr[start] > t){
          return start
      } else if (arr[end] > t){
          return end
      } else if (arr[end] < t){
          return end+1
      }
  }
  let mid = ~~((start+end)/2);
  if(arr[mid] == t) {
    return mid;
  }
  else if(t > arr[mid]){
    return binsrch(arr, t, mid+1, end)
  }
  else if(t < arr[mid]){
    return binsrch(arr, t, start, mid-1)
  }
}

var searchInsert = function(nums, target) {
  return binsrch(nums, target, 0, nums.length-1);
};