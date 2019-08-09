var findComplement = function(num) {
  let t = [];
  const rev = x => {
    let val = 1;
    let sum = 0;
    for(i=x.length-1;i>=0;i--){
      sum += x[i]*val;
      val = val*2;
    }
    return sum;
  }
  const rec = n => {
      if(n!==1 && n!==0){
          if(n % 2 == 0){
            t.push(0)
          }
          else{
            t.push(1)
          }
        rec(Math.floor(n/2));
      }
      else if(n == 1){
        t.push(0);
        rev(t);
      }
      else{
        t.push(1);
        rev(t);
      }

  }
  rec(num);
};

var findWords = function(words) {
  const row1 = new Set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']);
  const row2 = new Set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']);
  const row3 = new Set(['z', 'x', 'c', 'v', 'b', 'n', 'm']);
  let output = [];
  for(i=0;i<words.length;i++){
      let j = 0;
      let comp = true;
      let word = words[i].split('');
      let row = row1;
      word[0] = word[0].toLowerCase();
      let good = false;
      while(comp){
          if(j===0){
              if(row1.has(word[0])){
                  row = row1;
              }
              else if(row2.has(word[0])){
                  row = row2;
              }
              else if(row3.has(word[0])){
                  row = row3;
              }
          }
          else if(j === word.length){
              comp = false;
              good = false;
          }
          else if(row.has(word[j]) === false){
              comp = false;
          }
          else{
              j++;
          }
      }
      if(good){
          output.push(words[i])
      }
  }
  return output;
};

[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]