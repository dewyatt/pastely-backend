FROM alpine:latest
MAINTAINER Daniel Wyatt <Daniel.Wyatt@gmail.com>
LABEL Description="Pastely Backend - Alpine Base" Version="1.0"

ARG deploy_environment
ARG git_sha1

# Bootstrap by installing ansible
RUN apk add --no-cache ansible

# Run our playbook
COPY ansible /tmp/deploy
WORKDIR /tmp/deploy
RUN ansible-playbook --connection=local                                                         \
                     --extra-vars="deploy_environment=$deploy_environment git_sha1=$git_sha1"   \
                     -i localhost,                                                              \
                     site.yaml                                                                  \
                     -vv

EXPOSE 8000

WORKDIR /pastely
ENTRYPOINT venv/bin/uwsgi --ini /pastely/uwsgi.ini
