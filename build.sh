#!/usr/bin/env bash

pixi install # This makes sure lock file is up to date, otherwise you get errors "lock-file not up-to-date with the project" because we call pixi install --locked
docker buildx build --builder cloud-alexkreidler-default-builder -f docker/Dockerfile.cpu --push --tag alexkreidler/marker-server:1.0.2-cpu --platform linux/amd64,linux/arm64 --progress=plain .