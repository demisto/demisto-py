#!/usr/bin/env bash

# exit on errors
set -e

rm -rf demisto_client/demisto_api
rm -rf docs
mkdir -p demisto_client
mv README.md README.md.org
docker run --rm -it -v `pwd`:/work -w /work swaggerapi/swagger-codegen-cli:2.4.7 generate -i /work/server_api_swagger.json -l python -o /work -c /work/swagger-config.json
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
# Not clear why python fails on these imports
sed -i '' -e 's/^from demisto_client.demisto_api.models.advance_arg import AdvanceArg/# &/' demisto_client/demisto_api/models/operator_argument.py
sed -i '' -e 's/^from demisto_client.demisto_api.models.group import Group/# &/' demisto_client/demisto_api/models/groups.py
sed -i '' -e 's/^from demisto_client.demisto_api.models.investigation_playbook import InvestigationPlaybook/# &/' demisto_client/demisto_api/models/investigation_playbook_task.py
# __api_call needs to work with dict objects and not Classes when updating data such as POST requests
sed -i '' -e 's/config = self.configuration/&; body = body.to_dict() if hasattr(body, "to_dict") else body  # noqa: E702/' demisto_client/demisto_api/api_client.py
# Some Models return no data if datatype is not set
# sed -i '' -e '171 s/None/response_data/' demisto_client/demisto_api/api_client.py
# Update the docs
sed -i '' -e '/# demisto-py/,/## Documentation for API Endpoints/d' docs/README.md
echo '## Documentation for API Endpoints' | cat - docs/README.md > readme.temp && mv readme.temp docs/README.md
sed -i '' -e 's#(docs/#(#' docs/*.md
sed -i '' -e 's#(../README.md#(README.md#' docs/*.md
