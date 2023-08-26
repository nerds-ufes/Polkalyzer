#!/bin/bash

# Answer are you sure? if yes, then print "Restoring environment..." with case sensitive
read -p "Are you sure you want to restore the environment? (y/n)" answer
case $answer in
	y|Y)
		echo "Restoring environment..."
		git restore .
		git clean -fd
	;;
	n|N) echo "Aborting ..." ;;
	* )echo "Invalid Answer, aborting ..." ;;
esac
