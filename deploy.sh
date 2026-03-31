#!/bin/bash

VERSION=${1:-latest}
PORT=${2:-5000}
CONTAINER_NAME="devops-web"
IMAGE_NAME="devops-app:$VERSION"

echo "Déploiement version $VERSION sur le port $PORT..."

# Stop & remove ancien container
docker stop $CONTAINER_NAME 2>/dev/null
docker rm $CONTAINER_NAME 2>/dev/null

# Build image
if ! docker build -t $IMAGE_NAME .; then
    echo "Erreur lors du build ! Rollback effectué"
    exit 1
fi

# Run container
docker run -d -p $PORT:5000 --name $CONTAINER_NAME $IMAGE_NAME

echo "Déploiement terminé : version $VERSION sur localhost:$PORT"
