var MinStack = function() {
  this.items = [];
  this.minTracker = [];
  
};

/** 
* @param {number} x
* @return {void}
*/
MinStack.prototype.push = function(x) {
  this.items.push(x);
  let putIn = x;
  for(i=0;i<this.minTracker.length;i++){
      if(this.minTracker[i] > putIn){
          [putIn, this.minTracker[i]] = [this.minTracker[i], putIn]
      }
  }
  this.minTracker.push(putIn)
};

/**
* @return {void}
*/
MinStack.prototype.pop = function() {
  let t = this.items.pop();
  this.minTracker.splice(this.minTracker.indexOf(t), 1)
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
  return this.minTracker[0]
};