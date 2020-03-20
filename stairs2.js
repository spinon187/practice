const count = (n, memo) => {
  return memo[n] = 
    n < 0
      ? 0
    : n === 0
      ? 1
    : memo[n]
      ? memo[n]
    : count(n-1, memo) + count(n-2, memo)
}

const stairWrapper = n => {
  let memo = new Array(n);
  count(n, memo);
  console.log(memo[n]);
}

stairWrapper(7)