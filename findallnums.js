var findDisappearedNumbers = function(nums) {
  let k = new Set([...nums]), output = [], max = nums.length;
  for(let i = 1;i<=max;i++){
    if(!k.has(i)) output.push(i);
    if(i>max) max = i;
  }
  return output
};