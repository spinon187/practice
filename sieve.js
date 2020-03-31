if(n < 3) return 0;
let arr = new Array(n).fill(true), count = 0;
arr[0] = false, arr[1] = false;
for(i=2;i<n;i++){
  if(arr[i]){
    count++;
    curr = i+i;
    while(curr<n){
      arr[curr] = false;
      curr = curr+i
    }
  }
}
return count;