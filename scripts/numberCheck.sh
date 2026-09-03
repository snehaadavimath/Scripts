#!/bin//bash

number=$1

if [[ $number -gt 0 ]]; then
	echo "Number $number is Positive "
elif [[ "$number" -lt 0 ]]; then
	echo "Number $number is Negative"
else
	echo "Number is zero"
fi

