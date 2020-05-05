const minNumberOfFrogs = str => {
  let min = 0, indexes = {c: 0, r: 1, o: 2, a: 3}, storage = [[],[],[],[]];
  for(let i = 0; i<str.length; i++){
    if(str[i] === 'k'){
        for(let j = 0; j<storage.length; j++){
          if(!storage[j]) return -1;
          storage[j].pop()
        }
        min = Math.max(min, storage[0].length+1);
    } else {
      let tar = indexes[str[i]]
      for(let j = 0; j<=tar; j++){
        if(j === tar){
          storage[tar].push(1)
        } else if(!storage[j].length) {
          return -1
        }
      }
    }
  }
  for(let j = 0; j<storage.length; j++){
    if(storage[j].length) return -1
  }
  return min;
}