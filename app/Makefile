REGISTRY=83.166.247.130:5000
IMAGE=perpy-fastapi
VERSION?=v1
REGISTRY_USER?=change_me_user
REGISTRY_PASSWORD?=change_me_password
APP_NAME?=FastAPI Template
APP_ENV?=prod

.PHONY: login build build-local push bp

login:
	echo "$(REGISTRY_PASSWORD)" | docker login $(REGISTRY) --username $(REGISTRY_USER) --password-stdin

build:
	docker build --build-arg BUILD_VERSION=$(VERSION) --build-arg APP_NAME="$(APP_NAME)" --build-arg APP_ENV="$(APP_ENV)" -t $(REGISTRY)/$(IMAGE):$(VERSION) -t $(REGISTRY)/$(IMAGE):latest .

build-local:
	docker build --build-arg BUILD_VERSION=$(VERSION) --build-arg APP_NAME="$(APP_NAME)" --build-arg APP_ENV="$(APP_ENV)" -t $(IMAGE):$(VERSION) -t $(IMAGE):latest .

push:
	docker push $(REGISTRY)/$(IMAGE):$(VERSION)
	docker push $(REGISTRY)/$(IMAGE):latest

bp: login build push
