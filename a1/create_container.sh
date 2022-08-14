#!/bin/bash
# Creating the first container
mkdir ~/nautilus_ps
cd ~/nautilus_ps

# -i : keep [s][t]an[d]ard [i][n]put device open (which in this system will be the keyboard)
# -t : to use a teletype terminal
sudo docker run -it ubuntu:20.04
