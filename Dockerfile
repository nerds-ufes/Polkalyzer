FROM ubuntu:latest
RUN apt-get update && \
	apt-get install -y \
		python3 \
		python3-pip \
		sudo \ 
		systemctl \
		git \
		vim
RUN pip install --upgrade pip

WORKDIR /home
RUN git clone https://github.com/mininet/mininet
RUN git clone https://github.com/nerds-ufes/Polkalyzer.git

WORKDIR /home/mininet
RUN util/install.sh -a

WORKDIR /home/Polkalyzer
RUN git checkout develop
RUN pip install -r requirements.txt
CMD ["service","openvswitch-switch","start"]
CMD /bin/bash
