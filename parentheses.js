class Stack {
  constructor(){
    this.items = []
  }
  push(x){
    this.items.push(x)
  }
  pop(){
    return this.items.length ? this.items.pop() : 'stack empty'
  }
  peek(){
    return this.items[this.items.length-1]
  }
  empty(){
    return this.items.length === 0;
  }
}

const longest = s => {
  let start = 0, max = 0, stack = new Stack();
  for(i=0; i<s.length; i++){
    if(s[i] === '('){
      stack.push(i)
    } else {
      if(stack.empty()){
        start = i+1;
      } else {
        stack.pop();
        if(stack.empty()){
          max = Math.max(max, i-start+1)
        } else {
          max = Math.max(max, i-stack[stack.length-1])
        }
      }
    }
  }
  return max;
}