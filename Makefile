VERSION := $(shell git describe --tags --always --dirty)
IMAGE_NAME=digitalocean-ddns:${VERSION}

.PHONY: build push all

.DEFAULT_GOAL := all

build:
	@docker build -f docker/Dockerfile -t ${IMAGE_NAME}  .

push:
	@docker push sluehr/${IMAGE_NAME}

all: build push

