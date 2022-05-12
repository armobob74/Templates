#!/bin/bash
x=1
while [ $x -le 100 ]
do
  echo "This is a command of some sort"
  x=$(( $x + 1 ))
done
