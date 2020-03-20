const staircount = n => {
  let memo = new Array(n-1);
  memo[0] = 1;
  memo[1] = 1;
  memo[2] = 2;
  const recur = (x, mem) => {
    if(!mem[x-3]){
      mem[x-3] = recur(x-3, mem)
    };
    if(!mem[x-2]){
      mem[x-2] = recur(x-2, mem)
    };
    if(!mem[x-1]){
      mem[x-1] = recur(x-1, mem)
    };
    return mem[x-3]+mem[x-2]+mem[x-1];
  }
  return recur(n, memo);
}

/*5
1 1 1 1 1

2 1 1 1
1 2 1 1
1 1 2 1
1 1 1 2

2 2 1
2 1 2
1 2 2

3 1 1
1 3 1
1 1 3

2 3
3 2

4
1 1 1 1

1 1 2
1 2 1
2 1 1

2 2

3 1
3 3

6
1 1 1 1 1 1

2 1 1 1 1
1 2 1 1 1
1 1 2 1 1
1 1 1 2 1
1 1 1 1 2

2 2 1 1
2 1 2 1
2 1 1 2
1 2 2 1
1 2 1 2
1 2 2 2

3 1 1 1
1 3 1 1
1 1 3 1
1 1 1 3

3 2 1
3 1 2
2 3 1
1 3 2
1 2 3
2 1 3

3 3

7
1 1 1 1 1 1 1

2 1 1 1 1 1 x6

2 2 1 1 1
2 1 2 1 1
2 1 1 2 1
2 1 1 1 2

1 2 2 1 1
1 2 1 2 1
1 2 1 1 2

1 1 2 2 1
1 1 2 1 2

1 1 1 2 2

3 1 1 1 1 x5

3 2 1 1
3 1 2 1
3 1 1 2

2 3 1 1
2 1 3 1
2 1 1 3

1 2 3 1
1 2 1 3
1 2 1 3

1 1 2 3
1 1 3 2






*/