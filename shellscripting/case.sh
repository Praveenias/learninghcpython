#!/bin/bash
# Author : Praveen R
# Purpose : learning shell scripting
# Date : 07-Nov-2023
# Modification : 07-Nov-2023

echo "PLease select from a choise"

echo "A:ls,B:whoami,C:hostname"

read choise

case $choise in
A) date;;
B) whoami;;
C) hostname;;
*) echo "Invalid Option"

esac