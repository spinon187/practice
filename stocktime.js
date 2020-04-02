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

var maxProfit = function(prices) {
  let total = 0, low = 0, running = 0;
  for(i=0; i<prices.length; i++){
    if(prices[i] < prices[i-1]){
      if(running > 0) total += running;
      running = 0;
      low = i;
    } else {
      running = Math.max(running, prices[i]-prices[low])
    }
  }
  if(running > 0) total += running
  return total;
};