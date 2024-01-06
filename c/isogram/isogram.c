#include "isogram.h"
#include <stddef.h>
#include <ctype.h>

bool is_isogram( const char phrase[] ) {
  int i = 0;

  if ( phrase == NULL ) {
    return false;
  }

  bool isog = true;

  while ( phrase[i] != '\0' ) {

    if ( phrase[i] == '-' || phrase[i] == ' ') {
      i++;
      continue;
    }

    int j = i+1;

    while ( phrase[j] != '\0' ) {
      if ( phrase[j] == '-' || phrase[j] == ' ') {
        j++;
        continue;
      }
      if ( tolower(phrase[i]) == tolower(phrase[j]) ) {
        isog = false;
      }
      j++;
    }
    i++;
  }

  return isog;
}
