#!/usr/bin/env bash

# The following comments should help you get started:
# - Bash is flexible. You may use functions or write a "raw" script.
#
# - Complex code can be made easier to read by breaking it up
#   into functions, however this is sometimes overkill in bash.
#
# - You can find links about good style and other resources
#   for Bash in './README.md'. It came with this exercise.


   main () {
    if [[ $# -ne 2 ]]; then
      echo "Usage: hamming.sh <string1> <string2>"
      return 1
    fi
    arg1=$1 
    arg2=$2
    length1=${#arg1}
    length2=${#arg2}
    distance=0


    if [[ length1 -ne length2 ]]; then
      echo "strands must be of equal length"
      return 1
    fi 


     for ((i = 0; i < length1; i++)); do
       char1="${arg1:i:1}"
       char2="${arg2:i:1}"
       if [[ "$char1" != "$char2" ]]; then
         distance=$((distance+1))
       fi
     done

     echo $distance
   }


   main "$@"
