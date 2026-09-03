#!/bin/bash

dirName=$1
if [[ -d "$dirName"  ]]; then
	echo "Dir exists"
else
	mkdir "$dirName"
	echo "Dir created"
fi


