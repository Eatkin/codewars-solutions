// https://www.codewars.com/kata/5bc7bb444be9774f100000c3
// 2023-06-19T12:40:44.361+0000
class Version {
  constructor(ver = "0.0.1") {
    if (ver === "") {
      ver = "0.0.1";
    }
    // Parse version
    let vComponents = ver.split('.');
    while (vComponents.length < 3){
      vComponents.push(0);
    }
    
    for (let v of vComponents.slice(0,3)) {
      if (isNaN(parseInt(v))) {
        throw new Error("Error occured while parsing version!");
      }
    }
    
    [this.MAJOR, this.MINOR, this.PATCH] = vComponents;
    
    if (this.MAJOR + this.MINOR + this.PATCH === 0) {
      this.PATCH = 1;
    }
    
    this.history = [];
  }
  
  updateVersion() {
    this.history.push([this.MAJOR, this.MINOR, this.PATCH]);
  }
  
  major() {
    this.updateVersion();
    this.MAJOR++;
    this.MINOR = 0;
    this.PATCH = 0;
    return this;
  }
  
  minor() {
    this.updateVersion();
    this.MINOR++;
    this.PATCH = 0;
    return this;
  }
  
  patch() {
    this.updateVersion();
    this.PATCH++
    return this;
  }
  
  rollback() {
    try {
      [this.MAJOR, this.MINOR, this.PATCH] = this.history.pop();
      return this;
    }
    catch {
      throw new Error("Cannot rollback!");
    }
  }
  
  release() {
    return `${this.MAJOR}.${this.MINOR}.${this.PATCH}`;
  }
}

function vm(ver) {
  return new Version(ver);
}