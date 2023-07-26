#!/bin/bash

THRIFT_PORT=9090
cd ../flow_table

run(){
	for((i=1; i<=$1; i++)); #Hosts
	do
		simple_switch_CLI --thrift-port=$THRIFT_PORT < `find . -name "e$i.txt"`
		let 'THRIFT_PORT += 1 '
	done

	for((i=1; i<=$2; i++)); #Switches
	do
		simple_switch_CLI --thrift-port=$THRIFT_PORT < `find . -name "s$i.txt"`
		let 'THRIFT_PORT += 1 '
	done
}

run $1 $2
