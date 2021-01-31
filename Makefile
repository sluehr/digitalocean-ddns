VERSION := $(shell git describe --tags --always --dirty)
IMAGE_NAME=sluehr/digitalocean-ddns

.PHONY: build push all

.DEFAULT_GOAL := all

build:
	@docker build -f docker/Dockerfile -t ${IMAGE_NAME}:${VERSION} .
	@docker tag ${IMAGE_NAME}:${VERSION} ${IMAGE_NAME}:latest

push:
	@docker push ${IMAGE_NAME}:${VERSION}
	@docker push ${IMAGE_NAME}:latest

all: build push

