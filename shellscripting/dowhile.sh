#!/bin/bash
# Author : Praveen R
# Purpose : learning shell scripting
# Date : 07-Nov-2023
# Modification : 07-Nov-2023
i=0
while [ $i -lt 10 ]
do
  echo $i
  i=`expr $i + 1`
done