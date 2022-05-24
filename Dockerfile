FROM ubuntu:focal
RUN apt-get update && apt-get -y install tar wget xz-utils
RUN apt-get install -y curl git unzip wget
RUN apt install python3.8 -y

# RDP
RUN wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb
RUN git clone https://github.com/Avax00/cloud-RDP
RUN cd cloud-RDP
RUN python3 rdp.py
