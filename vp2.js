var isValid = function(s) {
  let stack = [];
  for(i=0;i<s.length;i++){
      if(s[i] == '(' || s[i] == '{' || s[i] == '['){
        stack.push(s[i])
      } else {
        if(s[i] == ')'){
          if(!stack.pop() == '('){
            return false;
          }
        }
        else if(s[i] == '}'){
          if(!stack.pop() == '{'){
            return false;
          }
        }
        else if(s[i] == ']'){
          if(!stack.pop() == '['){
            return false;
          }
        }
      }
  } return true;
};