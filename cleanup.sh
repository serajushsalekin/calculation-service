#!/bin/bash

echo "Performing cleanup..."

# Remove all Docker images
docker rmi -f $(docker images -aq)