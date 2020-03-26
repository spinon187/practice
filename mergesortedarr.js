const sort2 = (arr, i) => {
  while(arr[i] > arr[i+1]){
      [arr[i], arr[i+1]] = [arr[i+1], arr[i]];
      i++;
  }
  return arr;
}

var merge = function(nums1, m, nums2, n) {
  m = m-1, n = n-1;
  for(i=nums1.length-1;i>=0;i--){
    if(nums1[m] > nums2[n]){
      nums1[i] = nums1[m];
      m--;
    } else {
      nums1[1] = nums2[n];
      n--;
    }
    if(n<0) return nums1;
  }
};

