#!/bin/bash

# Answer are you sure? if yes, then restore the environment
echo "Are you sure you want to restore the environment? (y/n)" -p Answer
if [ "$Answer" != "${Answer#[Yy]}" ] ;then
	echo "Restoring environment..."
	git restore ../.
	git clean -fd ../.
