// https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1
using System;

public class Kata
{
  public static int GetAge(string inputString)
  {
    return int.Parse(inputString.Split(' ')[0]);
    // return correct age (int). Happy coding :)
  }
}