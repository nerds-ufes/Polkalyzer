#!/bin/bash

# Answer are you sure? if yes, then print "Restoring environment..." with case sensitive
read "Are you sure you want to restore the environment? (y/n)" -p answer
case $answer in
	[yY]* )
		echo "Restoring environment..."
		git restore .
		git clean -fd
	;;
	[nN]* ) exit;;
	* ) echo "Invalid Answer, aborting ...";;
esac
