var findMedianSortedArrays = function(nums1, nums2) {
  let total = nums1.length+nums2.length,
  target = ~~(total/2)+1,
  counter = 0,
  i = 0,
  j = 0;
  last = null, last2 = null;
  while(counter < target){
    last2 = last;
    if(i >= nums1.length){
      last = nums2[j];
      j++;
      counter++;
    } else if(j >= nums2.length){
      last = nums1[i];
      i++;
      counter++;
    } else if(nums1[i] < nums2[j]){
      last = nums1[i]
      i++;
      counter++
    } else if(nums1[i] >= nums2[j]){
      last = nums2[j];
      j++;
      counter++
    }
  }
  if(total%2){
    return last
  } else {
    return (last+last2)/2
  }
};