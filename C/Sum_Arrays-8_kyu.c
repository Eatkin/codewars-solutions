// https://www.codewars.com/kata/53dc54212259ed3d4f00071c
#include <stddef.h>

int sum_array(const int *values, size_t count)  {
  int i, sum;
  sum = 0;
  for (i = 0; i < count; i++)
    sum += values[i];
  
  return sum;
}