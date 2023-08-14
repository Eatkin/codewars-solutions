// https://www.codewars.com/kata/55b75fcf67e558d3750000a3
// 2023-06-19T11:01:59.530+0000
class Block{

  constructor(data){
    this.dimensions = data;
  }
  
  getWidth() {
    return this.dimensions[0];
  }
  
  getLength() {
    return this.dimensions[1];
  }
  
  getHeight() {
    return this.dimensions[2];
  }
  
  getVolume() {
    const [w, l, h] = this.dimensions;
    return l * w * h;
  }
  
  getSurfaceArea() {
    const [w, l, h] = this.dimensions;
    return 2 * (w * l + w * h + l * h);
  }
  
}