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
mv README.md.org README.md
# Not clear why python fails on these imports
sed -i '' -e 's/^from demisto_client.demisto_api.models.advance_arg import AdvanceArg/# &/' demisto_client/demisto_api/models/operator_argument.py
sed -i '' -e 's/^from demisto_client.demisto_api.models.group import Group/# &/' demisto_client/demisto_api/models/groups.py
sed -i '' -e 's/^from demisto_client.demisto_api.models.investigation_playbook import InvestigationPlaybook/# &/' demisto_client/demisto_api/models/investigation_playbook_task.py
# __api_call needs to work with dict objects and not Classes when updating data such as POST requests
sed -i '' -e 's/config = self.configuration/&; body = demisto_client.to_extended_dict(body)  # noqa: E702/' demisto_client/demisto_api/api_client.py
# Update the docs
sed -i '' -e '/# demisto-py/,/## Documentation for API Endpoints/d' docs/README.md
echo '## Documentation for API Endpoints' | cat - docs/README.md > readme.temp && mv readme.temp docs/README.md
sed -i '' -e 's#(docs/#(#' docs/*.md
sed -i '' -e 's#(../README.md#(README.md#g' docs/*.md
sed -i '' '/# Configure API key authorization: api_key/,/DefaultApi(demisto_client.demisto_api.ApiClient(configuration))/c\
api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")\
' docs/DefaultApi.md
sed -i '' -e '/import time/ a\
import demisto_client' docs/DefaultApi.md
# Remove the class name in the endpoint api table as it doesn't look good on github.com
sed -i '' -e 's#Class \| ##' docs/README.md
sed -i '' -e 's#^------------ \| ##' docs/README.md
sed -i '' -e 's#^\*DefaultApi\* \| ##g' docs/README.md
sed -i '' -e 's/^## Author//g' docs/README.md
# add ability for generic requests
sed -i '' -e 's/import six/import six\
import demisto_client/g' demisto_client/demisto_api/api/default_api.py
echo -e "\n    def generic_request(self, path, method, body=None, **kwargs):  # noqa: E501\n        return demisto_client.generic_request_func(self, path, method, body, **kwargs)" >> demisto_client/demisto_api/api/default_api.py
# fix bug where binary data is decoded on py3
sed -i '' -e 's#if six\.PY3:#if six.PY3 and r.getheader("Content-Type") != "application/octet-stream":#' demisto_client/demisto_api/rest.py

# Fix import layout command
start=`grep "verify the required parameter 'type'" demisto_client/demisto_api/api/default_api.py -n | cut -f1 -d: | tail -1 | tr -d "\\n"`
end=`grep ".kind. when calling .import_layout." demisto_client/demisto_api/api/default_api.py -n | cut -f1 -d: | tail -1 | tr -d "\\n"`
sed -i '' -e "$start,${end}d" demisto_client/demisto_api/api/default_api.py
kind_line=`grep "'kind' in params:" -n demisto_client/demisto_api/api/default_api.py | cut -f1 -d: | tr -d "\\n"`
start=$((kind_line-4))
end=$((kind_line+1))
sed -i '' -e "$start,$end s/if \(.*\) in params/if params.get(\1, None)/" demisto_client/demisto_api/api/default_api.py
sed -i '' -e "s:'/v2/layouts/import', 'POST',:demisto_client.get_layouts_url_for_demisto_version(self.api_client, params), 'POST',:" demisto_client/demisto_api/api/default_api.py

sed -i '' -e 's/def import_layout(self, file, type, kind, \*\*kwargs):/def import_layout(self, file, \*\*kwargs):/' demisto_client/demisto_api/api/default_api.py

sed -i '' -e '/import demisto_client/ a\
import json' demisto_client/demisto_api/api/default_api.py

ret_line=`grep "return self.import_layout_with_http_info" demisto_client/demisto_api/api/default_api.py -n | cut -f1 -d: | tail -1 | tr -d "\\n"`
start=$((ret_line-3))
sed -i '' -e "${start}a\\
\ \ \ \ \ \ \ \ with open(file, 'r') as layout_json_file:\\
\ \ \ \ \ \ \ \ \ \ \ \ data = layout_json_file.read()\\
\ \ \ \ \ \ \ \ layout_data_json = json.loads(data)\\
\ \ \ \ \ \ \ \ type = layout_data_json.get('typeId')\\
\ \ \ \ \ \ \ \ kind = layout_data_json.get('kind')" demisto_client/demisto_api/api/default_api.py

# End fix import layout

# remove files not used
rm .travis.yml
rm git_push.sh
