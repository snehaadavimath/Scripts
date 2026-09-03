#!/bin/bash

fileName=$1

if [[ -z "$fileName" ]]; then
	echo "File exists $fileName"
else
	echo "File does not exists"
fi


