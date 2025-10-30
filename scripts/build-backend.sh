#!/bin/bash
# Build script for backend

echo "=== Building Backend Image ==="

# Build production image
docker build -t rfi-backend:latest -f backend/Dockerfile backend/

# Build development image
docker build -t rfi-backend:dev -f backend/Dockerfile.dev backend/

echo " Backend images built successfully!"
docker images | grep rfi-backend
