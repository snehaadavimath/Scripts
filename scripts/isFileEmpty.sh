#!/bin/bash

fileName=$1

if [[ -s $fileName ]] ; then

	echo "File is not empty"
else
	echo "File is empty"
fi



