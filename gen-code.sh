#!/bin/bash
rm -r demisto_client/demisto_api
rm -r demisto_client/docs
mkdir demisto_client
docker run --rm -it -v `pwd`:/work -w /work swaggerapi/swagger-codegen-cli generate -i /work/server_api_swagger.json -l python -o /work/demisto_client -c /work/swagger-config.json
rm -r demisto_client/test
