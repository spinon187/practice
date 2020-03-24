const checkLeft = (i, arr, iList, count) => {
  let found = false, val = 0, j = i-1;
  while(!found && j>=0){
    if(arr[j] >= arr[i]){
      found = true;
    }
    else {
      val++;
      j--;
    }
  }
  if(!iList.has([j, i])){
    iList.add([j, i]);
    return found ? [iList, count+val] : [iList, count];
  } else {
    return [iList, count]
  }

}

const checkRight = (i, arr, iList, count) => {
  let found = false, val = 0, j = i+1;
  while(!found && j<arr.length){
    if(arr[j] >= arr[i]){
      found = true;
      iList.add([i, j])
    }
    else {
      val++;
      j++;
    }
  }
  return found ? [iList, count+val] : [iList, count];
}

var trap = function(height) {
  let iList = new Set(), count = 0;
  for(i=0;i<height.length;i++){
    [iList, count] = checkLeft(i, height, iList, count);
    [iList, count] = checkRight(i, height, iList, count);
  }
  return count;
};