FROM ubuntu:latest

ENV BM_SSWITCH /home/Polkalyzer/lib/p4/bmv2/targets/simple_switch/
ENV PATH $BM_SSWITCH:$PATH

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
RUN git pull origin develop # Prevent cache conflicts
RUN pip install -r requirements.txt
RUN service openvswitch-switch start
CMD ["service","openvswitch-switch","start"]
CMD /bin/bash
