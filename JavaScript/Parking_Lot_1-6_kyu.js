// https://www.codewars.com/kata/633701c187ca520016eec664
// 2023-06-19T13:42:56.083+0000
class ParkingLot {
  constructor(size) {
    this.size = size;
    this.spaces = new Array(size).fill(0);
  }
  
  park(vehicle) {
    // Find the first available space
    let vehicleSize = (vehicle instanceof Bike) ? 1 : ((vehicle instanceof Car) ? 2 : 3);
    let spacesUsed = 0;
    let spaceFound = false;
    let spaceIndex = 0;
    for (let i = 0; i < this.size; i++) {
      if (this.spaces[i] === 0) {
        if (spacesUsed === 0) {
          spaceIndex = i;
        }
        spacesUsed++;
        if (spacesUsed === vehicleSize) {
          spaceFound = true;
          break;
        }
      }
      else {
        spacesUsed = 0;
      }
    }
    
    if (!spaceFound) {
      return false;
    }
    
    // We've saved our spot in spaceIndex so let's pop the vehicle in by it's registration
    for (let i = spaceIndex; i < spaceIndex + vehicleSize; i++) {
      this.spaces[i] = vehicle.license;
    }
    return true;
  }
  retrieve(license) {
    // Loop through to find the vehicle
    let vehicleFound = false;
    for (let i = 0; i < this.size; i++) {
      // If we find the license scrub through until we remove it
      if (this.spaces[i] === license) {
        vehicleFound = true;
        this.spaces[i] = 0;
      }
      else if (vehicleFound) {
        break;
      }
    }
    
    return vehicleFound;
  }
}