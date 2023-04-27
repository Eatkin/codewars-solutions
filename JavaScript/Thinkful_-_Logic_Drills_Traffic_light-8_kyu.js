// https://www.codewars.com/kata/58649884a1659ed6cb000072
function updateLight(current) {
  const lights = ["green", "yellow", "red"];
  return lights[(lights.indexOf(current) + 1) % lights.length]
}