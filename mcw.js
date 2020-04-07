var mostCommonWord = function(paragraph, banned) {
  let d = {}, max = [0, null], abc = new Set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']), word = '';
  banned = new Set([...banned])
  for(let i in paragraph){
    if(abc.has(paragraph[i])){
      word += paragraph[i].toLowerCase()
    }
    else if(word.length) {
      if(!banned.has(word)){
        d[word] = d[word] ? d[word]+1 : 1;
        if(max[0] < d[word]){
          max = [d[word], word]
        }
      }
      word = ''
    }
  }
  return max[1] ? max[1] : word.toLowerCase()
};