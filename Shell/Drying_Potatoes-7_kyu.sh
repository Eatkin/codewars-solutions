# https://www.codewars.com/kata/58ce8725c835848ad6000007
#!/bin/bash
pi=$1
w=$2
pf=$3

echo "$w*(100-$pi)/(100-$pf)" | bc