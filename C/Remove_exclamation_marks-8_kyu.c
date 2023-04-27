// https://www.codewars.com/kata/57a0885cbb9944e24c00008e
#include <string.h>

// Write resulting string into buffer pointed by str_out
void remove_exclamation_marks(const char* str_in, char* str_out) {
	int count = 0;
	for (int i = 0; i < strlen(str_in); i++) {
		if (str_in[i] != '!') {
			str_out[count] = str_in[i];
			count++;
		}
	}
  
  str_out[count] = '\0';
}