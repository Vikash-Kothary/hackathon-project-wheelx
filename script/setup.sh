#!/bin/bash
# setup.sh

wget -O - https://bit.ly/docker-install | bash

sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo service docker restart
newgrp docker