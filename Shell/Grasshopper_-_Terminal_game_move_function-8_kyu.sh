# https://www.codewars.com/kata/563a631f7cbbc236cf0000c2
position=$1
roll=$2
# your code here
move()  {
  echo $((position + 2 * roll))
}

move