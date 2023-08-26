#!/bin/bash
docker build -t polkalyzer .
docker run -it --name polkalyzer --privileged polkalyzer
