#!/bin/bash
docker build -t polkalyzer . || sudo docker build -t polkalyzer .
docker run -it --name polkalyzer --privileged polkalyzer || sudo docker run -it --name polkalyzer --privileged polkalyzer
