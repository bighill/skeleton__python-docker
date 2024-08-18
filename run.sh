#!/bin/bash

# docker build -t py .
docker build --quiet -t py .

docker run --rm -it py