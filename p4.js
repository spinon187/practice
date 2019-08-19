var singleNumber = function(nums) {
    let yes = new Set();
    let no = new Set();
    let output = [];
    for(i=0;i<nums.length;i++){
      if(!no.has(nums[i])){
        if(yes.has(nums[i])){
          yes.delete(nums[i]);
          no.add(nums[i])
        }
        else{
          yes.add(nums[i])
        }
      }
    }
    yes.forEach(num => output.push(num));
    return output;
};

// var frequencySort = function(s) {
//   let dict = {};
//   s = s.split('');
//   for(i=0;i<s.length;i++){
//       if(!dict.hasOwnProperty(s[i])){
//           dict[s[i]] = s[i];
//       }
//       else{
//           dict[s[i]] += s[i];
//       }
//   }
//   s = Object.values(dict);
//   s.sort((a,b) => (b.length-a.length)).join('');
//   return s;  
// };

// var frequencySort = function(s) {
//   let dict = new Map();
//   s = s.split('');
//   for(i=0;i<s.length;i++){
//       if(!dict.has(s[i])){
//           dict.set(s[i], s[i]);
//       }
//       else{
//           dict.set(s[i],dict.get(s[i])+s[i]);
//       }
//   }
//   s = Map.values(dict);
//   s.sort((a,b) => (b.length-a.length)).join('');
//   return s;  
// };
