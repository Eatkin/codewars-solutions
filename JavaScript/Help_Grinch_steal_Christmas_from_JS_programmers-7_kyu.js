// https://www.codewars.com/kata/63387232198a4c00286aa349
// 2023-06-19T11:15:17.028+0000
Date.prototype.getDate = function getGrinchDate() {
  const dateStr = this.toString();
  
  // This matches the first number which is usefully the date
  const match = dateStr.match(/\d+/);
  
  const date = parseInt(match[0])
    
  if (this.getMonth() === 11 && date === 25)
    return 26;
  
  return date;
}