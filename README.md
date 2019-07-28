# Provenance Service
<sup>`develop` branch status: </sup>[![Build Status](https://travis-ci.com/Sage-Bionetworks/prov-service.svg?branch=master)](https://travis-ci.com/Sage-Bionetworks/prov-service) [![Coverage Status](https://coveralls.io/repos/github/Sage-Bionetworks/prov-service/badge.svg?branch=master&service=github)](https://coveralls.io/github/Sage-Bionetworks/prov-service?branch=master&service=github)

Lightweight implementation of the Synapse Activity services, based on the PROV spec.

## Overview

This is an OpenAPI-enabled (and documented) Flask server. This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask. The [py2neo]() driver library for Python is used to manage operations between RESTful API requests/responses and a Neo4j database.

This server was originally generated by the [OpenAPI Generator](https://openapi-generator.tech) project. Starting with the Synapse Activity API specification in a `swagger.yaml` file, the contents of this repo were originally generated with the following command:

```shell
npx openapi-generator generate -i swagger.yaml -g python-flask -DpackageName=synprov -o prov-service/
```

## Requirements

Python 3.5.2+

You should have access to a local installation of Neo4j, serving at `bolt://localhost/7687`<sup>*</sup>.

You'll also need to set two environment variables based on your Neo4j configuration (the Flask app uses these to connect to the database):

```shell
export NEO4J_USERNAME=<username> # must be 'neo4j'
export NEO4J_PASSWORD=<password>
```

</sup>*</sup>In some cases, the **Neo4j Desktop** app decides to serve the database on port `11001` instead of `7687`. If this happens, you can set an additional environment variable:

```shell
export NEO4J_PORT=11001
```

## Usage

To run the server, please execute the following from the root directory:

```shell
pip install -r requirements.txt .
```

To start the app, you can use this command:
```shell
synprov
```

To initialize the graph database with mock activity records, you can run the app with additional parameters:
```shell
synprov --mock_db --db_size 30
```

To view the full set of parameters:
```shell
synprov --help
```

```shell
Usage: synprov [OPTIONS]

Options:
  --mock_db          Initialize Neo4j database with mock graph records
                     [default: False]
  --db_size INTEGER  Number of mock activity records to create in the graph
                     database (ignored if 'init_db' is False).  [default: 50]
  --help             Show this message and exit.
```

### Neo4j browser

If you have the **Neo4j Desktop** application installed, you should be able to view and explore the graph database using Cypher queries. For example, to view all nodes and relationships:

```cypher
MATCH (n) RETURN n
```

Assuming that you populated the graph database with mock/example records as described above, you should see something that looks like this (minus the custom colors):

![example provenance graph](img/mockprov.png)


### Swagger UI

You can also interact with the graph database through RESTful API queries. The service provides a Swagger UI endpoint to test requests through the browser:

```
http://localhost:8080/rest/ui/
```

*If the above URL doesn't work, try this instead:*
```
http://0.0.0.0:8080/rest/ui/
```

![provenance swagger ui](img/swaggerui.png)


The OpenAPI definition lives here:

```
http://localhost:8080/rest/openapi.json
```

## Running with Docker

To run the server on a Docker container, execute the following from the root directory:

```shell
docker-compose up --build
```

> **Note:** In order to use the server container, which requires a Neo4j database connection, you should have [Docker Compose](https://docs.docker.com/compose/overview/) installed.

After running this command, the URLs in the previous section should work.

## Development

To add changes locally, install the package in developer mode:
```shell
pip install -r requirements.txt -e .
```

### OpenAPI Generator

The core `models` and `controllers` for the server are generated automatically from the OpenAPI specification. Classses and methods used for operations within the app all inherit from auto-generated definitions.

Anytime the OpenAPI spec is modified, controller and model code should be regenerated with the following command:

```shell
npx openapi-generator generate \
    -c .openapi-generator-config \
    -t .codegen/server \
    -Dmodels \
    -DmodelTests=false \
    -Dapis \
    -DapiTests=false \
    -i synprov/openapi/openapi.yaml \
    -g python-flask \
    -o .
```

**Note:** this will happen during the continuous integration process regardless, so regenerating and testing locally is just advised to save time troubleshooting.

