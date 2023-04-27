// https://www.codewars.com/kata/55a2d7ebe362935a210000b2
#include <stddef.h>

int find_smallest_int(const int array[/* len */], size_t len)
{
    int smallest = array[0];
    for (int i = 1; i < len; i++)
    {
        if (array[i] < smallest)
        {
			smallest = array[i];
		}
	}
    return smallest;
}