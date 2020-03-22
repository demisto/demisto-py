# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/demisto-py/#history
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
