// https://www.codewars.com/kata/5b4070144d7d8bbfe7000001
// 2023-06-13T09:16:38.608+0000
function numericals(s){
  const counts = {};
  let output_s = "";
  for (let letter of s) {
    if (counts.hasOwnProperty(letter)) {
      counts[letter]++;
    }
    else {
      counts[letter] = 1;
    }
    output_s += `${counts[letter]}`;
  }
  return output_s;
}