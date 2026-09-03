#!/bin/bash

url=$1

filename=$(basename "$url")

wget "$url"

ls -sh "$filename"

