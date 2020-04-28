var maxEqualFreq = function(nums) {
  let k = {}, f = {};
  for(let i = 0; i<nums.length; i++){
    let x = nums[i];
    k[x] = k[x]+1 || 1;
  }
  let vals = Object.values(k)
  for(let i = 0; i<vals.length; i++){
    let x = vals[i];
    f[x] = f[x]+1 || 1;
  }
  let max = 0, checked, vals2 = Object.keys(vals).sort((a,b)=>a-b)
  for(let i = 0; i<vals2.length;i++){
    let x  = vals2[i];
    max = Math.max(max, (nums.length-checked)*x);
    checked += vals[x];
  }
  return max === nums.length ? nums.length : max+1
};