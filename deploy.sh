#!/bin/bash

# exit on errors
set -e

function deploy_to_pypi () {
    git checkout .
    pip3 install twine wheel
    python3 setup.py sdist bdist_wheel
    TWINE_USERNAME=__token__ twine upload dist/*
}
function deploy_to_pypi_po () {
    git checkout .
    poetry build
    poetry publish -u __token__ -p ${PYPI_TOKEN}
}

if [[ "${CIRCLE_BRANCH}" == "master" ]]; then
    echo "Deploying to Pypi test site."
    TWINE_REPOSITORY_URL=https://test.pypi.org/legacy/ TWINE_PASSWORD="${PYPI_TEST_TOKEN}" deploy_to_pypi
elif [[ $(echo "${CIRCLE_TAG}" | grep -E "^v[0-9]+\.[0-9]+\.[0-9]+$") ]]; then
    echo "Deploying to Pypi production site"
    TWINE_PASSWORD="${PYPI_TOKEN}" deploy_to_pypi
else
    echo "Skipping Pypi deploy as we are not building a tag or on master"
fi
