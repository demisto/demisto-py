#!/bin/bash

rm -r demisto_client/demisto_api
rm -r docs
mkdir demisto_client
mv README.md README.md.org
docker run --rm -it -v `pwd`:/work -w /work swaggerapi/swagger-codegen-cli generate -i /work/server_api_swagger.json -l python -o /work -c /work/swagger-config.json
rm -r test
mv demisto_client.demisto_api/*.py demisto_client/demisto_api/.
mv demisto_client.demisto_api/api/*.py demisto_client/demisto_api/api/.
mv demisto_client.demisto_api/models/*.py demisto_client/demisto_api/models/.
rmdir demisto_client.demisto_api/api
rmdir demisto_client.demisto_api/models
rmdir demisto_client.demisto_api
mv README.md docs/.
# TODO: need to fix back links to README.md
mv README.md.org README.md
