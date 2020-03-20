const shiftM = (arr, add, remove, m1, m2=null, extra=0) => {

  if(!m2){
    let i=m1, old = m1;
    if(remove > m1 && add < m1){
      if(arr[m1] - extra > 1){
        extra++
      }
      else {
        while(m1 === old){
          if(arr[i] > 0){
            m1 = i;
            extra = 0;
          } else {
            i--;
          }
        }
      }
    } else if(remove < m1 && add > m1) {
      if(extra){
        extra--
      } else {
        while(m1 === old){
          if(arr[i] < 0){
            m1 = i;
            extra = 0;
          } else {
            i++;
          }
        }
      }
    }
  } else {
    if(remove >= m1 && add <= m1){
      let i = m1, old = m1;
      m2 = m1;
      if(arr[m1] - extra > 1){
        extra++
      } else {
        while(m1 === old){
          if(arr[i] > 0){
            m1 = i;
            extra = 0;
          } else {
            i--;
          }
        }
      }
    } else if(remove <= m1 && add >= m1) {
      let i = m2, old = m2;
      m1 = m2;
      if(extra > 1){
        extra--
      } else {
        while(m2 === old){
          if(arr[i] < 0){
            m2 = i;
            extra = 0;
          } else {
            i++;
          }
        }
      }
    }
  }
  return [m1, m2, extra];
}

const countSort = (arr, countArr, m1= null, m2= null, add=null, remove=null, extra = null) => {
  if(!countArr){
    let medTar = ~~(arr.length/2), medCount = 0;
    countArr = new Array(201);
    countArr.fill(0);
    for(let i = 0; i<arr.length;i++){
      countArr[arr[i]]++

    }
    let i = 0;
    while(medCount < medTar){
      if(countArr[i] > 0){
        medCount += countArr[i];
      }
      if(medCount >= medTar){        
        m1 = i;
        extra = medCount-medTar;
        if(medTar%2){
          if(extra){
            m2 = i
          }
          else{
            while(!m2){
              i++;
              if(arr[i]>0) m2 = i;
            }
          }
        }
      }
      i++;
    }

  }
  if(add){
    countArr[add] = countArr[add]+1;
    countArr[remove] = countArr[remove]-1;
    [m1, m2, extra] = shiftM(countArr, add, remove, m1, m2, extra);
  }
  return [countArr, m1, m2, extra]
}

class Queue {
  constructor(storage){
    this.storage = storage;
  }
  enq(el){
    this.storage.push(el)
  }
  deq(){
    return this.storage.shift()
  }
  front(){
    return this.storage[0]
  }
  back(){
    return this.storage[this.storage.length-1]
  }
}


// Complete the activityNotifications function below.
function activityNotifications(expenditure, d) {
  let count = 0, values = expenditure.slice(0,d), min = 0, max = 200, m1=null, m2=null, extra=0, queue = new Queue(values), countArr;

  [countArr, m1, m2, extra] = countSort(values, countArr, m1, m2, null, null, extra);

  for(let i=d;i<expenditure.length;i++){
    let val = expenditure[i];
    console.log(values);
    if(!d%2){
      count = val >= m1+m2 ? count+1 : count;
    } else {
      count = val >= m1*2 ? count+1 : count;
    }
    [countArr, m1, m2, extra] = countSort(null, countArr, m1, m2, val, queue.front(), extra);
    queue.deq();
    queue.enq(val);
  }
  return count;
}