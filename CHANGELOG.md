# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/demisto-py/#history
## 3.0.0
* Drop support for Python 2. demisto-py now requires Python 3.7 or later. Pin to demisto-py <2.0.24 to maintain 2.7 support.
* Fixed bug in arguments required for the route: `/v2/inv-playbook/task/form/submit`.

## 2.0.23
* Support for adding feed indicators via the route: `/indicators/feed/json`.

## 2.0.22
* Don't cache last response in case `DONT_CACHE_LAST_RESPONSE` environment variable is set to true, this to avoid memory leaks.

## 2.0.20
* Log only headers in exceptions when `DEMISTO_EXCEPTION_HEADER_LOGGING` environment variable is set to true. This protects against possible sensitive data being logged in exceptions.


## 2.0.19
* Support `import_layout` to upload the new layout version(layoutscontainer).
* Fixed `import_layout` when uploading an old layout version.
* Removed testing with Python 3.6 and added testing with Python 3.8.
* Added to the `generic_request` function support for `response_type` argument.


## 2.0.14
Fixed an issue where the attribute mapping for the `search_incidents` model was incorrectly looking for `incidents` not `data`.

## 2.0.13
* Fixed the `filter` parameter in `search_incidents` method to be required as specified in the API.

## 2.0.12
* Fixed a bug in the `import_layout` method where an API endpoint was not working as planned.

## 2.0.11
* Added `import_playbook` method for importing a playbook to Demisto.
* Added `import_script` method for importing a script to Demisto.
* Added `import_incident_fields` method for importing an incident field to Demisto.
* Added `import_incident_types_handler` method for importing an incident type to Demisto.
* Added `import_widget` method for import a widget to Demisto.
* Added `import_dashboard` method for import a dashboard to Demisto.
* Added `import_classifier` method for importing a classifier to Demisto.
* Added `import_layout` method for importing a layout to Demisto.


## 2.0.10
* Enabled host and path parameters to function with trailing or leading slashes.

## 2.0.9
* Improved error message when missing authentication parameters.

## 2.0.8
* Added `ssl_ca_cert` configuration option to specify an alternate certificate bundle.
* Added support for additional configuration environment variables:
  * `DEMISTO_VERIFY_SSL`
  * `SSL_CERT_FILE`

## 2.0.7
* Added `investigation_add_entries_sync` method creating a new entry in existing investigation.
* Added `download_file` method for downloading files by entry id.
* Added `integration_upload` method for uploading integrations to Demisto.

## 2.0.6
Added support for user/password authentication option.

## 2.0.5
Removed unsupported user/password authentication option.

## 2.0.4
Fixed missing dependency (tzlocal).

## 2.0.3
* Fixed issue in `generic_request` where body was being ignored ([#20](https://github.com/demisto/demisto-py/issues/20)) .
* Added `content_type` and `accept` parameters to `generic_request`.
* Fixed `datetime` object formatting to include timezone offset as specified in RFC 3339.

## 2.0.2
* Support for environment variables when configuring the client.
* Updated `create_incident` with CustomFields and removed invalid `attachment` parameter.
* Added `incident_file_upload` method for uploading files to an incident.

## 2.0.1
Improved the changelog and documentation.

## 2.0.0
Initial release of new Swagger based API for Demisto Server 4.5.0 and up.

## 1.0.0
Deprecated: demisto-py 1.x is officially in maintenance-mode only and can be obtained at: https://github.com/demisto/demisto-py/releases .
