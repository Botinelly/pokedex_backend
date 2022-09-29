FROM python:3.7-slim

RUN useradd -rm -d /home/pokedex -s /bin/bash -g root -G sudo -u 1000 pokedex

RUN export DEBIAN_FRONTEND=noninteractive && \
apt-get -y update && \
apt-get install -y \
gcc \
libssl-dev \ 
make

WORKDIR /usr/pokedex/app

RUN chown -R pokedex /usr/pokedex/app

USER pokedex

COPY . ./

RUN pip install --no-cache-dir --no-warn-script-location -r requirements.txt 

ENV PATH=$PATH:/home/pokedex/.local/bin

CMD python -u main.py

