var findMedianSortedArrays = function(nums1, nums2) {
  let total = nums1.length+nums2.length,
  target = ~~(total/2),
  counter = 0,
  i=0,
  j=0;
  while(counter < target){
    if(nums1[i] < nums2[j]){
      i++;
      counter++
    } else if(nums1[i] > nums2[j]){
      j++;
      counter++
    }
  }
  if(total%2){
    return Math.min(nums1[i], nums1[j])
  } else {
    let arr = [nums1[i], nums1[i+1], nums2[j], nums2[j+1]],
    v1 = Math.min(...arr);
    arr.splice(arr.indexOf(v1, 1));
    let v2 = Math.min(...arr);
    return [v1, v2]
  }
};