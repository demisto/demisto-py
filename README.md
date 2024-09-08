# Demisto Client for Python

[![PyPI version](https://badge.fury.io/py/demisto-py.svg)](https://badge.fury.io/py/demisto-py)
![Build and Release workflow](https://github.com/demisto/demisto-py/actions/workflows/main.yml/badge.svg)


A Python library for the Demisto API.

Version 2.x is compatible with Demisto server version 4.5 and later.

## Demisto for Python Usage

This section covers the steps you need to take to get the client configured.

### 1. Get a Demisto API Key

Follow these instructions to generate your Demisto API Key.

1. In Demisto, navigate to **Settings > API Keys**.
2. Click the **Generate Your Key** button.

To avoid hard coding configurations in your code, it is possible to specify configuration params
as the following environment variables (env variables will be used if parameters are not specified):

* DEMISTO_BASE_URL
* DEMISTO_API_KEY
* DEMISTO_ADVANCED_API_KEY
* DEMISTO_USERNAME
* DEMISTO_PASSWORD
* DEMISTO_HTTP_HEADERS (must be in the form of: header1=value1,header2=value2,header3=value3,...headerN=valueN)
* DEMISTO_VERIFY_SSL (true/false. Default: true)
* DEMISTO_API_KEY_ID (for Cortex XSIAM only. If set, Cortex XSIAM API will be used)
* SSL_CERT_FILE (specify an alternate certificate bundle)

### 2. Create a Demisto client instance with the api-key and server-url

```python
import demisto_client

# Also possible to set env variables: DEMISTO_API_KEY and DEMISTO_BASE_URL
api_key = 'YOUR_API_KEY'
host = 'https://YOUR_DEMISTO_HOST'

api_instance = demisto_client.configure(base_url=host, api_key=api_key)

```

**For Cortex XSIAM, we need to set the auth_id**
```python
import demisto_client

# Also possible to set env variables: DEMISTO_API_KEY, DEMISTO_BASE_URL and DEMISTO_API_KEY_ID
api_key = 'YOUR_API_KEY'
auth_id = 'THE AUTHORIZATION ID'
host = 'https://YOUR_XSIAM_HOST'

api_instance = demisto_client.configure(base_url=host, api_key=api_key, auth_id=auth_id)

```

**Alternatively, you can login with username and password (only in xsoar):**

```python
import demisto_client

# Also possible to set env variables: DEMISTO_USERNAME DEMISTO_PASSWORD and DEMISTO_BASE_URL
host = 'https://YOUR_DEMISTO_HOST'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'

api_instance = demisto_client.configure(base_url=host, username=username, password=password)
```

### 3. Create incidents

```python
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException


api_key = 'YOUR_API_KEY'
host = 'https://YOUR_DEMISTO_HOST'

api_instance = demisto_client.configure(base_url=host, api_key=api_key, debug=False)
create_incident_request = demisto_client.demisto_api.CreateIncidentRequest()

create_incident_request.name = 'Sample Simulation Incident'
create_incident_request.type = 'Simulation'
create_incident_request.owner = 'Admin'

try:
    api_response = api_instance.create_incident(create_incident_request=create_incident_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_incident: %s\n" % e)

```

Additional examples available in the [docs](docs/README.md) and under the [examples folder](examples/).

---

## API Documentation

API Documentation based upon the Demisto Server Swagger API is available [here](docs/README.md)

---

## Troubleshooting

### API Key

If when using an API key you encounter a response similar to the following:

```json
{"id":"forbidden","status":403,"title":"Forbidden","detail":"Issue with CSRF code","error":"http: named cookie not present","encrypted":false,"multires":null}
```

It means your API key is invalid. Make sure you are using a valid API key. You can check your API key by using curl with the following request:

```bash
  curl -i -k -H 'Authorization: YOUR_API_KEY'  https://your-demisto.server.url/about
```

For a valid API key you will receive a response similar to the following:

```BASH
HTTP/1.1 200 OK
Strict-Transport-Security: max-age=10886400000000000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Xss-Protection: 1; mode=block
Date: Thu, 04 Jun 2020 09:27:53 GMT
Content-Length: 189
Content-Type: text/plain; charset=utf-8

{"demistoVersion":"5.5.0", ...}
```

---

## Contributing

Contributions are welcome and appreciated. To contribute follow the instructions below and submit a PR.

Before merging any PRs, we need all contributors to sign a contributor license agreement. By signing a contributor license agreement, we ensure that the community is free to use your contributions.

When you open a new pull request, a bot will evaluate whether you have signed the CLA. If required, the bot will comment on the pull request, including a link to accept the agreement. The CLA document is also available for review as a [PDF](https://github.com/demisto/content/blob/master/docs/cla.pdf).

If the `license/cla` status check remains on *Pending*, even though all contributors have accepted the CLA, you can recheck the CLA status by visiting the following link (replace **[PRID]** with the ID of your PR): <https://cla-assistant.io/check/demisto/demisto-py?pullRequest=[PRID>] .

---

## Dev Environment Setup

We will now setup a quick virtualenv in which we will install the `demisto-py` version you are currently working on.
This will be used as your testing environment, you do not need to update it again or re-run in any way.

1. Make sure you have python3 installed.

2. Make sure you have [Poetry](https://python-poetry.org/) installed.

3. run `poetry install`

4. For further reading about Poetry, you can refer to [Poetry documentation](https://python-poetry.org/).

You have now setup the your `demisto-py` dev environment!

To activate it simply run: `poetry shell`.

To deactivate the virtual environment and return simply run: `exit`.

---

## Running unit-tests using Pytest

We use [pytest](https://github.com/pytest-dev/pytest) to run unit tests.

Simply use `poetry` to run your tests on a relevant folder. For example:
```
poetry run python -m pytest tests
```

To run with a specific python version (see the [demisto-py PyPi page](https://pypi.org/project/demisto-py/) for the current supported versions), use [poetry environments](https://python-poetry.org/docs/managing-environments/) to switch to a different env with a different python version.

---


## Code Generation

Library code was generated using the Demisto Server 4.5.0 Swagger definition with modifications to support later Server versions.

**Important:** All code under [demisto_client/demisto_api](demisto_client/demisto_api) is generated using the swagger code generation tool. Do not modify this code directly.

We use a script to run the generate tool and then modify as needed.
If you would like to contribute **DO NOT** modify the generated code directly, modify the script: [gen-code.sh](gen-code.sh) and then re-generate the code.

To generate the code run (requires bash, sed and docker):

```bash
./gen-code.sh
```

---

## Publishing a Release (demisto devs)

After merging to `master`, a test deployment will be pushed to: <https://test.pypi.org/project/demisto-py/> .
You can test the test package by following the pip install instructions.
For example:

```bash
pip install -i https://test.pypi.org/simple/ demisto-py
```

Steps to publish a production release:

* Make sure [CHANGELOG.md](CHANGELOG.md) is up to date.
* Update the version number in the `pyproject.toml` file to the new version.
* Create and push a tag with the release version using git.
For example:

  ```bash
  git tag v2.0.19
  git push origin v2.0.19
  ```

* Check that the circleci build completes successfully. Once done, the release will be pushed to: <https://pypi.org/project/demisto-py/> .
* Update GitHub releases: go to [tags page](https://github.com/demisto/demisto-py/tags) and for the relevant tag choose from the right drop down menu: `Create release`. Name the release the same as the tag. Copy the text from previous releases for the description.

Congratulations! The release is now public.

---
## License

Apache 2.0 - See [LICENSE](LICENSE) for more information.
