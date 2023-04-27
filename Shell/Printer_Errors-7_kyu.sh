# https://www.codewars.com/kata/56541980fa08ab47a0000040
#!/bin/bash
printerError() {
    echo $(echo $1 | grep -o [^a-m] | wc -l)"/"${#1}
}
printerError $1