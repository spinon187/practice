const binSrch = (s, e, f) => {
  while(s<=e){
    let m = ~~((s+e)/2);
    let val = f(m);
    if(val){
        if(!f(m-1) || m-1 < 1){
            return m
        } else {
            e = m
        }
    } else {
        s = m
    }
  }
  // if(e-s === 1){
  //     if(f(s)){
  //         return s
  //     } else {
  //         return e
  //     }
  // }
  // let m = ~~((s+e)/2);
  // let val = f(m);
  // if(val){
  //     if(!f(m-1) || m-1 < 1){
  //         return m
  //     } else {
  //         return binSrch(s, m, f)
  //     }
  // } else {
  //     return binSrch(m, e, f)
  // }
}

var solution = function(isBadVersion) {
  /**
   * @param {integer} n Total versions
   * @return {integer} The first bad version
   */
  return function(n) {
      return binSrch(1, n, isBadVersion)
  };
};