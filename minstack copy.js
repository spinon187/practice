
class MinHeap {
  constructor(){
    this.storage = []
  }
  insert = x => {
    this.storage.push(x);
    this.bubbleUp(this.storage.length-1)
  }
  bubbleUp = i => {
    while(i>0){
      let p = ~~((i+1)/2) - 1;
      if(this.storage[p] > this.storage[i]){
        [this.storage[p], this.storage[i]] = [this.storage[i], this.storage[p]]
      }
      i = p;
    }
  }
  getMin = () => {
    return this.storage[0]
  }
  
}

var MinStack = function() {
  this.items = [];
  this.dummy = new LLNode(null);
};

/** 
* @param {number} x
* @return {void}
*/
MinStack.prototype.push = function(x) {
  this.items.push(x);
  // for(i=0;i<this.minTracker.length;i++){
  //     if(this.minTracker[i] > putIn){
  //         [putIn, this.minTracker[i]] = [this.minTracker[i], putIn]
  //     }
  // }
  // this.minTracker.push(putIn)
  if(!this.dummy.next){
    this.dummy.next = new LLNode(x)
  } else {
    let curr = this.dummy.next, prev = this.dummy;
    while(curr){
      if(curr.val < x){
        if(!curr.next){
          curr.next = new LLNode(x)
        } else {
          prev = curr;
          curr = curr.next;
        }
      } else if (curr.val > x){
        let n = new LLNode(x);
        prev.next = n;
        n.next = curr;
        break;
      }
    } 
  }
};

/**
* @return {void}
*/
MinStack.prototype.pop = function() {
  let t = this.items.pop();
  let curr = this.dummy.next, prev = this.dummy;
  while(curr){
    if(curr.val = t){
      prev.next = curr.next;
    } else {
      prev = curr;
      curr = curr.next;
    }
  }
};

/**
* @return {number}
*/
MinStack.prototype.top = function() {
  return this.items[this.items.length-1]
};

/**
* @return {number}
*/
MinStack.prototype.getMin = function() {
  return this.dummy.next;
};