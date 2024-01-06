#include "armstrong_numbers.h"
#include <stdio.h>
#include <math.h>

bool is_armstrong_number(int candidate);

bool is_armstrong_number(int candidate) {
  if ( candidate == 0 ) {
    return true;
  }

  int iterations = 0;
  int sum = 0;
  int candidateCopy = candidate;
  int arr[20];

  for ( int i=10; i <= candidate*10; i *= 10 ) {
    int digit = (candidateCopy % i) / (i / 10);
    arr[iterations] = digit;
    iterations += 1;
    candidateCopy -= candidateCopy % i;
  }

  for ( int i = 0; i < iterations; i++ ) {
    sum += pow(arr[i], iterations);
  }

  bool armstrong = (double) candidate == sum;

  return armstrong;
}
