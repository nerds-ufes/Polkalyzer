#!/bin/bash
docker compose run app || \
docker-compose run app || \
sudo docker compose run app || \
sudo docker-compose run app || \
echo "Error: docker-compose not found, please install docker-compose"
