var maxProfit = function(prices) {
  let low = 0, max = 0;
  for(i=1;i<prices.length;i++){
      if(prices[i] < prices[low]){
          low = i;
      } else {
          max = Math.max(max, prices[i]-prices[low])
      }
  }
  return max;
};