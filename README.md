# Docker Examples

This repository contains a few helpful examples for exploring Docker.

## JavaScript

* `javascript` - contains a client and server application using Node/Express and Vue3. This is an example of using Docker Compose to create a database container that can be used during local development. This project is also ready to use the `docker init` command to add the Docker files to the server for deployment.

* `js-docker` - contains the same application that has been set up for deployment using Docker. This goes beyond the `docker init` command by demonstrating a two-phase build process. 

## Python

* `python` - contains a client and server application using Poetry/Flask and Vue3. This is an example of using Docker Compose to create a database container that can be used during local development. This project is also ready to use the `docker init` command to add the Docker files to the server for deployment. 

* `py-docker` - contains the same application that has been set up for deployment using Docker. This goes beyond the `docker init` command by demonstrating a two-phase build process. 

## Deploy

* `deploy` - this folder contains a sample deployment of these containers using Docker Compose, [Traefik Proxy](https://traefik.io/traefik/), [Watchtower](https://containrrr.dev/watchtower/), and [Docker Socket Proxy](https://github.com/Tecnativa/docker-socket-proxy). Sample configurations are also included. 

* `.github/workflows` - this contains a sample workflow to automatically generate releases and Docker containers when a semantic version tag (such as `v0.1.2`) is pushed to GitHub. It can also trigger a deployment via webhook to Watchtower. 

Each subfolder has individual `README.md` files with more information. 
