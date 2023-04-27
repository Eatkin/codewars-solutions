// https://www.codewars.com/kata/5bb904724c47249b10000131
function points(games) {
  return games.reduce(function(points, str) {
      // Extract scores
      const [ourScore, opponentScore] = str.split(":").map(Number);
      // Return points based on score difference
      return (ourScore > opponentScore) ? points + 3  : (ourScore === opponentScore) ? points + 1 : points;
    },0);
}