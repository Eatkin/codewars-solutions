// https://www.codewars.com/kata/5601409514fc93442500010b
const betterThanAverage = (classPoints, yourPoints) => classPoints.reduce((i, point) => i + point, 0) / classPoints.length < yourPoints;
