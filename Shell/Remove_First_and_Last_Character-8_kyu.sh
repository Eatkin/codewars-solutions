# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
function removeChar() {
  local str=$1
  echo "${str:1:-1}"
}
removeChar $1