#!/bin/bash
echo "Starting docker container ..."
docker start polkalyzer || sudo docker start polkalyzer
echo "Running terminal on docker container ..."
docker exec -it polkalyzer /bin/bash || sudo docker exec -it polkalyzer /bin/bash
echo "Stoping docker container, please wait a while ..."
docker stop polkalyzer || sudo docker stop polkalyzer
