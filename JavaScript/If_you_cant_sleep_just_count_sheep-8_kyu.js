// https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
var countSheep = function (num){
  let sheepString = "";
  for (let i = 1; i <= num; i++)
    sheepString +=  `${i} sheep...`;
  
  return sheepString;
}