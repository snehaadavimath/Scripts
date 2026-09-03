#!/bin/bash
#set -x
url=$1

fileName=$(basename "$url")

wget "$url"


if [[ -f $fileName ]]; then
	#set -x
	fileSize=$(du -h "$fileName" | cut -f1)
	echo "File name: $fileName"
	echo "File Size: $fileSize"
fi
