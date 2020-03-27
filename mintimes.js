// const objectify = arr => {
//   let o = {};
//   for(let i = 0; i<arr.length; i++){
//     o[i] = !o[i] ? 1 : o[i]+1
//   }
//   return o;
// }

// function minTime(machines, goal) {
//   let count = 0, days = 0;
//   machines = objectify(machines);
//   while(count < goal){
//     days++
//     for(let i = 1; i<=Math.sqrt(days); i++){
//       if(days%i === 0){
//         let i2 = days/i;
//         if(i !== i2){
//           if(machines[i]) count += machines[i];
//           if(machines[i2]) count += machines[i2]
//         } else {
//           if(machines[i]) count += machines[i]
//         }
//       }
//     }
//   }
//   return days;
// }