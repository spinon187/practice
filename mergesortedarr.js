const sort2 = (arr, i) => {
  while(arr[i] > arr[i+1]){
      [arr[i], arr[i+1]] = [arr[i+1], arr[i]];
      i++;
  }
  return arr;
}

var merge = function(nums1, m, nums2, n) {
  let j = 0, i=0;
  for(i;i<m;i++){
      if(nums1[i] > nums2[j]){
          [nums1[i], nums2[j]] = [nums2[j], nums1[i]];
          nums2 = sort2(nums2, 0)
      }
  }
  for(i;i<nums1.length;i++){
      [nums1[i], nums2[j]] = [nums2[j], nums1[i]];
      j++
  }
  return nums1;
};