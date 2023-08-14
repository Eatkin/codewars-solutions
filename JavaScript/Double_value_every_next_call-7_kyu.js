// https://www.codewars.com/kata/632408defa1507004aa4f2b5
// 2023-06-19T11:05:45.701+0000
class Class {
  static value = 1;
  
  static getNumber() {
    const v = this.value;
    this.value *= 2;
    return v;
  }
}