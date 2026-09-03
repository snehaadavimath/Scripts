#!/bin/bash


num1=$1
num2=$2


if [[ $# -eq 2 ]]; then

	if [[ "$num1" -gt "$num2" ]]; then
		echo "$num1 is greater than $num2"
	else 
		echo "$num1 is less than $num2"
	fi
fi
