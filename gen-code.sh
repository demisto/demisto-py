#!/usr/bin/env bash

# ALL CHANGES TO GENERATE CODE ARE DONE VIA THIS FILE

# exit on errors
set -e

# IMPORTANT: Make sure when writing sed command to use: sed -i "${INPLACE[@]}"
# to be compatible with mac and linux
# sed on mac requires '' as param and on linux doesn't
if [[ "$(uname)" == Linux ]]; then
    INPLACE=()
else
    INPLACE=('')
fi

rm -rf demisto_client/demisto_api
rm -rf docs
mkdir -p demisto_client
mv README.md README.md.org
docker run --rm -it -u `id -u` -v `pwd`:/work -w /work swaggerapi/swagger-codegen-cli:2.4.7 generate -i /work/server_api_swagger.json -l python -o /work -c /work/swagger-config.json
rm -rf test
mv demisto_client.demisto_api/*.py demisto_client/demisto_api/.
mv demisto_client.demisto_api/api/*.py demisto_client/demisto_api/api/.
mv demisto_client.demisto_api/models/*.py demisto_client/demisto_api/models/.
rmdir demisto_client.demisto_api/api
rmdir demisto_client.demisto_api/models
rmdir demisto_client.demisto_api
mv README.md docs/.
mv README.md.org README.md
# Not clear why python fails on these imports
sed -i "${INPLACE[@]}" -e 's/^from demisto_client.demisto_api.models.advance_arg import AdvanceArg/# &/' demisto_client/demisto_api/models/operator_argument.py
sed -i "${INPLACE[@]}" -e 's/^from demisto_client.demisto_api.models.group import Group/# &/' demisto_client/demisto_api/models/groups.py
sed -i "${INPLACE[@]}" -e 's/^from demisto_client.demisto_api.models.investigation_playbook import InvestigationPlaybook/# &/' demisto_client/demisto_api/models/investigation_playbook_task.py
# __api_call needs to work with dict objects and not Classes when updating data such as POST requests
sed -i "${INPLACE[@]}" -e 's/config = self.configuration/&; body = demisto_client.to_extended_dict(body)  # noqa: E702/' demisto_client/demisto_api/api_client.py
# Update the docs
sed -i "${INPLACE[@]}" -e '/# demisto-py/,/## Documentation for API Endpoints/d' docs/README.md
echo '## Documentation for API Endpoints' | cat - docs/README.md > readme.temp && mv readme.temp docs/README.md
sed -i "${INPLACE[@]}" -e 's#(docs/#(#' docs/*.md
sed -i "${INPLACE[@]}" -e 's#(../README.md#(README.md#g' docs/*.md
sed -i "${INPLACE[@]}" -e '/# Configure API key authorization: api_key/,/DefaultApi(demisto_client.demisto_api.ApiClient(configuration))/c\
api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")' docs/DefaultApi.md
sed -i "${INPLACE[@]}" -e '/import time/ a\
import demisto_client' docs/DefaultApi.md
sed -i "${INPLACE[@]}" -e 's/> InstanceClassifier import_classifier(file, classifier_id)/> InstanceClassifier import_classifier(file)/' docs/DefaultApi.md
sed -i "${INPLACE[@]}" -e 's/api_response = api_instance.import_classifier(file, classifier_id)/api_response = api_instance.import_classifier(file)/' docs/DefaultApi.md
sed -i "${INPLACE[@]}" -e 's/> LayoutAPI import_layout(file, type, kind)/> LayoutAPI import_layout(file)/' docs/DefaultApi.md
sed -i "${INPLACE[@]}" -e 's/api_response = api_instance.import_layout(file, type, kind)/api_response = api_instance.import_layout(file)/' docs/DefaultApi.md
del=`grep  "\*\*type\*\* | \*\*str\*\*| associated typeID for the layout | " docs/DefaultApi.md -n | head -n1 | cut -d : -f1`
sed -i "${INPLACE[@]}" -e "$del d" docs/DefaultApi.md
del=`grep  "\*\*kind\*\* | \*\*str\*\*| layout kind details | " docs/DefaultApi.md -n | head -n1 | cut -d : -f1`
sed -i "${INPLACE[@]}" -e "$del d" docs/DefaultApi.md

# Remove the class name in the endpoint api table as it doesn't look good on github.com
sed -i "${INPLACE[@]}" -e 's#Class \| ##' docs/README.md
sed -i "${INPLACE[@]}" -e 's#^------------ \| ##' docs/README.md
sed -i "${INPLACE[@]}" -e 's#^\*DefaultApi\* \| ##g' docs/README.md
sed -i "${INPLACE[@]}" -e 's/^## Author//g' docs/README.md
# add ability for generic requests
sed -i "${INPLACE[@]}" -e 's/import six/import six\
import demisto_client/g' demisto_client/demisto_api/api/default_api.py
echo -e "\n    def generic_request(self, path, method, body=None, **kwargs):  # noqa: E501\n        return demisto_client.generic_request_func(self, path, method, body, **kwargs)" >> demisto_client/demisto_api/api/default_api.py
# fix bug where binary data is decoded on py3
sed -i "${INPLACE[@]}" -e 's#if six\.PY3:#if six.PY3 and r.getheader("Content-Type") != "application/octet-stream":#' demisto_client/demisto_api/rest.py
# Disable sensitive logging by default
sed -i "${INPLACE[@]}" -e 's/import ssl/import ssl\
import os/g' demisto_client/demisto_api/rest.py
sed -i "${INPLACE[@]}" -e 's/"""Custom error messages for exception"""/"""Custom error messages for exception"""\
        sensitive_env = os.getenv("DEMISTO_EXCEPTION_HEADER_LOGGING")\
        if sensitive_env:\
            sensitive_logging = sensitive_env.lower() in ["true", "1", "yes"]\
        else:\
            sensitive_logging = False/' demisto_client/demisto_api/rest.py
sed -i "${INPLACE[@]}" -e 's#        if self.headers:#        if self.headers and sensitive_logging:#' demisto_client/demisto_api/rest.py
# Fix import layout command
start=`grep "verify the required parameter 'type'" demisto_client/demisto_api/api/default_api.py -n | cut -f1 -d: | tail -1 | tr -d "\\n"`
end=`grep ".kind. when calling .import_layout." demisto_client/demisto_api/api/default_api.py -n | cut -f1 -d: | tail -1 | tr -d "\\n"`
sed -i "${INPLACE[@]}" -e "$start,${end}d" demisto_client/demisto_api/api/default_api.py
kind_line=`grep "'kind' in params:" -n demisto_client/demisto_api/api/default_api.py | cut -f1 -d: | tr -d "\\n"`
start=$((kind_line-4))
end=$((kind_line+1))
sed -i "${INPLACE[@]}" -e "$start,$end s/if \(.*\) in params/if params.get(\1, None)/" demisto_client/demisto_api/api/default_api.py
sed -i "${INPLACE[@]}" -e "s:'/v2/layouts/import', 'POST',:demisto_client.get_layouts_url_for_demisto_version(self.api_client, params), 'POST',:" demisto_client/demisto_api/api/default_api.py

sed -i "${INPLACE[@]}" -e 's/def import_layout(self, file, type, kind, \*\*kwargs):/def import_layout(self, file, \*\*kwargs):/' demisto_client/demisto_api/api/default_api.py

sed -i "${INPLACE[@]}" -e '/import demisto_client/ a\
import json' demisto_client/demisto_api/api/default_api.py

ret_line=`grep "return self.import_layout_with_http_info" demisto_client/demisto_api/api/default_api.py -n | cut -f1 -d: | tail -1 | tr -d "\\n"`
start=$((ret_line-3))
sed -i "${INPLACE[@]}" -e "${start}a\\
\ \ \ \ \ \ \ \ with open(file, 'r') as layout_json_file:\\
\ \ \ \ \ \ \ \ \ \ \ \ data = layout_json_file.read()\\
\ \ \ \ \ \ \ \ layout_data_json = json.loads(data)\\
\ \ \ \ \ \ \ \ type = layout_data_json.get('typeId')\\
\ \ \ \ \ \ \ \ kind = layout_data_json.get('kind')" demisto_client/demisto_api/api/default_api.py

# End fix import layout

# fix import_classifier
sed -i "${INPLACE[@]}" -e 's/def import_classifier(self, file, classifier_id, \*\*kwargs):  # noqa: E501/def import_classifier(self, file, \*\*kwargs):  # noqa: E501/' demisto_client/demisto_api/api/default_api.py
sed -i "${INPLACE[@]}" -e 's/>>> thread = api.import_classifier(file, classifier_id, async_req=True)/>>> thread = api.import_classifier(file, async_req=True)/' demisto_client/demisto_api/api/default_api.py
del=`grep ":param str classifier_id: associated typeID for the layout (required)" demisto_client/demisto_api/api/default_api.py -n | head -n1 | cut -d : -f1`
sed -i "${INPLACE[@]}" -e "$del d" demisto_client/demisto_api/api/default_api.py

select=`grep "return self.import_classifier_with_http_info(file, classifier_id, \*\*kwargs)  # noqa: E501" demisto_client/demisto_api/api/default_api.py -n | head -n1 | cut -d : -f1`
start=$((select-2))
sed -i "${INPLACE[@]}" -e "${start}a\\
\ \ \ \ \ \ \ \ with open(file, 'r') as classifier_json_file:\\
\ \ \ \ \ \ \ \ \ \ \ \ data = classifier_json_file.read()\\
\ \ \ \ \ \ \ \ classifier_data_json = json.loads(data)\\
\ \ \ \ \ \ \ \ classifier_id = classifier_data_json.get('id')" demisto_client/demisto_api/api/default_api.py

sed -i "${INPLACE[@]}" -e 's/PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types/CACHE_LAST_RESPONSE = not os.environ.get("DONT_CACHE_LAST_RESPONSE", False)\
    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types/' -e 's/self.last_response = response_data/if self.CACHE_LAST_RESPONSE:\
            self.last_response = response_data/' demisto_client/demisto_api/api_client.py
# End fix import_classifier

# remove files not used
rm .travis.yml
rm git_push.sh

echo "# DO NOT MODIFY CODE IN THIS DIRECTORY OR SUB-DIRS.

Use gen-code.sh to perform any changes needed in generated code.

" > demisto_client/demisto_api/README.md
