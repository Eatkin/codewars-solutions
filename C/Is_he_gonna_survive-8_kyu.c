// https://www.codewars.com/kata/59ca8246d751df55cc00014c
#include <stdbool.h>
#include <stdint.h>

bool hero(uint32_t bullets, uint32_t dragons) {
  return (bullets >= dragons * 2) ? true : false;
}