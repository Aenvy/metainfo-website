# CMS5G metainfo website

Welcome to the CMS5G Metainfo Website repository, housing both frontend (ReactJS) and backend (Python) components, Dockerized and managed through a unified Docker Compose configuration. The live deployment of this website can be accessed at [HPE MC5G Solutions website](https://ktm215.gre.hpecorp.net/)

## Overview

This project offers a streamlined development and deployment ecosystem for the metainfo website, featuring distinct frontend and backend elements. Leveraging Docker and Docker Compose ensures a consistent setup process across diverse environments

## Key Features

* Dockerized ReactJS frontend and Python Backend.
* Unified Docker Compose configuration for managing both frontend and backend services.
* Deployment-ready setup for hosting the website at https://ktm215.gre.hpecorp.net.

## Prerequisites

Before diving in, make sure you have the following prerequisites:

* Docker
* Docker Compose

## Getting Started

Let's kickstart the process:

1. Clone the repository:

```console
$ git clone https://github.hpe.com/cms5g/mc5g-metainfo-website.git
```

2. Navigate to the project directory:
```console
$ cd mc5g-metainfo-website
```

## Configuration

Before executing Docker commands, ensure necessary configurations are in place:

1. Frontend configuration:

```console
$ cp mc5g-metainfo-website-frontend/src/config.js.sample config.js
```
2. Backend environment variables:
```console
$ cp mc5g-metainfo-website-backend/conf/rbac.yaml.sample rbac.yaml
$ cp mc5g-metainfo-website-backend/conf/jenkins.yaml.sample jenkins.yaml
$ cp mc5g-metainfo-website-backend/conf/.env.sample .env
```
3. Update the .env file with required environment variables. Refer to the [Backend documentation](mc5g-metainfo-website-backend/README.md) for details.

## Setting Up HTTPS Protocol with Certificate and Key

To enable HTTPS protocol for secure communication between the client and server, follow these steps:
1. Obtain the HPE SSL certificate and private key.
2. Create a fullchain.pem
```console
$ sudo cp ~/ktm215.key /etc/pki/tls/private/
$ sudo cat ~/ktm215.cer /etc/pki/ca-trust/source/anchors/HP_Ent_Private_SSL_CA.cer > /home/cmssdmci/certs.d/ktm215-fullchain.pem
```
3. Create a volume using docker compose (either in [docker-compose-production.yml](docker-compose-production.yml) or [docker-compose-sandbox.yml](docker-compose-sanbox.yml), depending on the environment) and update it with appropriate paths to the fullchain.pem and key.
### Environment for production
```yaml
environment:
  - CERTFILE=/var/certs.d/ktm215-fullchain.pem
  - KEYFILE=/var/certs.d/ktm215.key
```
### Environment for sandbox
```yaml
environment:
  - CERTFILE=/var/certs.d/ktm442-fullchain.pem
  - KEYFILE=/var/certs.d/ktm442.key
```

## Test Frontend deployment

To test the front end deployment, follow the intructions outlined in [Start Application](mc5g-metainfo-website-frontend/README.md#npm-start) and [Test Application](mc5g-metainfo-website-frontend/README.md#npm-test)

## Dockerfile

The dockerfile builds two images
1. Frontend using node20
2. Backend using python3.12

The frontend is constructed according to the instructions outlined in [Build Application](mc5g-metainfo-website-frontend/README.md#npm-run-build), resulting in a build directory containing all necessary files for the frontend website to function on the hosted domain.

Subsequently, the Dockerfile copies the build directory to the backend Python image, which deploys the website using the Python app [backend.py](mc5g-metainfo-website-backend/src/backend.py).

## Deployment

To deploy the website to [HPE MC5G Solutions website](https://ktm215.gre.hpecorp.net/), execute the following command:
```console
$ docker-compose up -d --build
```
Ensure smooth sailing by adhering to these instructions. 