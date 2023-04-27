// https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
function past(h, m, s){
  let seconds = s + 60 * (m + 60 * h);
  return seconds * 1000;  //1s = 1000ms
}