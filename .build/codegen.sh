#!/usr/bin/env bash

OPENAPI_PATH=synprov/openapi/openapi.yaml

docker run --rm \
    -v ${PWD}:/local openapi-generator generate \
    -c /local/.openapi-generator-config \
    -t /local/.codegen/server \
    -Dmodels \
    -DmodelTests=false \
    -Dapis \
    -DapiTests=false \
    -i /local/synprov/openapi/openapi.yaml \
    -g python-flask \
    -o /local/