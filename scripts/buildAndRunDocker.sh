#!/bin/bash
docker build -t polkalyzer . || sudo docker build -t polkalyzer .
docker run -it --name polkalyzer --rm --privileged -e DISPLAY polkalyzer || sudo docker run -it --name polkalyzer --rm --privileged -e DISPLAY polkalyzer
