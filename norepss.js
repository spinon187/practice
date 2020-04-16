var lengthOfLongestSubstring = function(s) {
  let max = 0, running = [], k = new Set();
  for(let i in s){
    if(!k.has(s[i])){
      k.add(s[i]);
      running.push(s[i])
    } else {
      max = Math.max(max, running.length);
      running = running.slice(running.indexOf(s[i])+1)
      running.push(s[i]);
      k = new Set([...running])
    }
  }
  return Math.max(max, running.length)
};