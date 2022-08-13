# base image
FROM ubuntu:20.04

# we'll use bash
SHELL ["/bin/bash", "-c"]

# first commands on tty in ubuntu:20.04 (update and install tmux)
RUN apt update && apt install tmux -y

# set mouse behavior on tmux
RUN echo "set -g mouse on" >> /root/.tmux.conf

# when open container go to /root
WORKDIR /root
