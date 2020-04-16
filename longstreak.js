const streak = (s, x, m) => {
  m = 1;
  s.delete(x)
  if(s.has(x+1)) m += streak(s, x+1, m);
  if(s.has(x-1)) m += streak(s, x-1, m);
  return m;
}


var longestConsecutive = function(nums) {
  nums = new Set([...nums]);
  let max = 0;
  nums.forEach(x => max = Math.max(max, streak(nums, x, 0)));
  return max;
};