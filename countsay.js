/**
 * @param {number} n
 * @return {string}
 */
const getCS = x => {
  let count = 0, val=x[0], output = '';
  for(let i in x){
    if(x[i] !== val){
      output = output + count + val;
      count = 1;
      val = x[i]
    } else {
      count++
    }
  }
  output = output + count + val;
  return output;
}

var countAndSay = function(n) {
    let x = '1';
    for(i=1;i<n;i++){
      x = getCS(x)
    }
    return x
};