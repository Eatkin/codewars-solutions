// https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
function reverseWords(str) {
  // Split by space
  let words = str.split(/\s/g);
  for (let i = 0; i < words.length; i++)
      words[i] = words[i].split("").reverse().join("")

  return words.join(" ")
}