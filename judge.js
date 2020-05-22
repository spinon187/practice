// class Node {
//   constructor(val){
//     val,
//     trusts = [],
//     trustedBy = []
//   }
// }

var findJudge = function(N, trust) {
  let k = {};
  for(let i = 1; i<=N; i++){
    // k[i] = new Node(i)
    k[i] = {trusted: [], trustedBy: []}
  };
  for(let i = 0; i<trust.length; i++){
    let a = trust[i][0], b = trust[i][1];
    k[a].trusts.push(b);
    k[b].trustedBy.push(a);
  }
  for(let i = 1; i<=N; i++){
    if(!k[i].trusts && k[i].trustedBy.length === N-1){
      return i
    }
  }
  return -1
};