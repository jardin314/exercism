#!/usr/bin/env bash

   main () {
    acronym=""
    str=$1
    upperStr=${str^^}
    upperStr=${upperStr//_ /}
    length=${#upperStr}
    lastIsSeparator=true

    for ((i=0; i < length; i++)); do
      chr=${upperStr:i:1}
     if [[ $lastIsSeparator == true && $chr != " " && $chr != "-" && $chr != "_" && $chr != "*" ]]; then
       acronym="${acronym}${upperStr:i:1}"
     fi
     if [[ ${upperStr:i:1} == " " || ${upperStr:i:1} == "-" ]]; then
       lastIsSeparator=true
      else
        lastIsSeparator=false
      fi
    done
    echo $acronym
   }

# call main with all of the positional arguments
   main "$@"
