import os
import unittest
import pytest
from urllib3_mock import Responses
import demisto_client
from datetime import datetime
import json
import urllib3
import tempfile
from demisto_client.demisto_api import rest

responses = Responses('requests.packages.urllib3')

api_key = 'sample_api_key'
host = 'http://localhost:8080'


def assert_reset():
    assert len(responses._urls) == 0
    assert len(responses.calls) == 0


def get_login_mocker(mocker, num_of_http_requests_mock: int=0):
    from urllib3 import PoolManager

    raw_http_responses = [
        urllib3.response.HTTPResponse(body=b'{}', status=200, headers={'Set-Cookie': 'XSRF-TOKEN=1234;'}),
        urllib3.response.HTTPResponse(body=b'{}', status=200, headers={'Set-Cookie': '1234'}),
    ]

    for i in range(num_of_http_requests_mock):
        raw_http_responses.append(
            urllib3.response.HTTPResponse(body=b'{}', status=200)
        )

    return mocker.patch.object(PoolManager, 'request', side_effect=raw_http_responses)


def test_get_docker_images():
    '''Check GET docker images.'''

    @responses.activate
    def run():
        body = '{ "images": [{"id": "aae7b8aaba8c", "repository": ' \
               '"openapitools/openapi-generator-cli", "tag": "latest", "createdSince": "3 days ago", ' \
               '"createdAt": "2019-08-19 13:34:22 +0300 IDT", "size": "131MB" }]}'
        responses.add('GET', '/settings/docker-images',
                      body=body,
                      status=200,
                      content_type='application/json')

        # create an instance of the API class
        api_instance = demisto_client.configure(base_url=host, api_key=api_key)
        api_response = api_instance.get_docker_images()

        assert api_response.images[0].created_at == '2019-08-19 13:34:22 +0300 IDT'
        assert api_response.images[0].id == 'aae7b8aaba8c'
        assert api_response.images[0].repository == 'openapitools/openapi-generator-cli'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == '/settings/docker-images'
        assert responses.calls[0].request.host == 'localhost'
        assert responses.calls[0].request.scheme == 'http'

    run()
    assert_reset()


def test_create_incident():
    '''Check creating an incident.'''

    @responses.activate
    def run():
        body = '{"name":"Test Incident","owner":"Admin","parent":"","phase":"",' \
               '"playbookId":"playbook0","playbook_id":"playbook0","rawCategory":"",' \
               '"rawCloseReason":"","rawJSON":"","rawName":"Test Incident","rawPhase":"",' \
               '"rawType":"Unclassified","raw_category":"","raw_close_reason":"","raw_json":"",' \
               '"raw_name":"Test Incident","raw_phase":"","raw_type":"Unclassified","reason":"",' \
               '"runStatus":"","run_status":"","severity":0,"sourceBrand":"Manual",' \
               '"sourceInstance":"admin","source_brand":"Manual","source_instance":"admin",' \
               '"status":0,"type":"Unclassified","version":1}'
        responses.add('POST', '/incident',
                      body=body,
                      status=200,
                      content_type='application/json')

        # create an instance of the API class
        api_instance = demisto_client.configure(base_url=host, api_key=api_key)
        create_incident_request = demisto_client.demisto_api.CreateIncidentRequest()
        create_incident_request.name = 'Test Incident'
        create_incident_request.type = 'Unclassified'
        create_incident_request.owner = 'Admin'
        create_incident_request.occurred = datetime.now()
        api_response = api_instance.create_incident(create_incident_request=create_incident_request)

        assert api_response.name == 'Test Incident'
        assert api_response.type == 'Unclassified'
        assert api_response.owner == 'Admin'

        assert len(responses.calls) == 1
        req = responses.calls[0].request
        assert req.url == '/incident'
        assert req.host == 'localhost'
        assert req.scheme == 'http'
        # veriy date field occurred according to rfc 3339
        req_body = json.loads(req.body)
        assert req_body['occurred'][-6] == '+' or req_body['occurred'][-6] == '-'  # end with +/- offset 

    run()
    assert_reset()


def test_get_reports():
    '''Testing GET all reports.'''

    @responses.activate
    def run():
        body = '[{"created_by":"DBot","dashboard":"None","decoder":{},"description":"This report ' \
               'generates Mean Time to Resolve by Incident type for last 2 Quarters",' \
               '"id":"MTTRbyIncidentType2Quar","locked":false,"name":"Mean time to Resolve by ' \
               'Incident Type (Last 2 Quarters)","orientation":"portrait","prev_name":"Mean time to ' \
               'Resolve by Incident Type (Last 2 Quarters)","prev_type":"pdf","type":"pdf",' \
               '"version":4}]'

        responses.add('GET', '/reports',
                      body=body,
                      status=200,
                      content_type='application/json')

        api_instance = demisto_client.configure(base_url=host, api_key=api_key, debug=False)
        api_response = api_instance.get_all_reports()

        assert api_response[0].id == 'MTTRbyIncidentType2Quar'
        assert api_response[
                   0].description == 'This report generates Mean Time to Resolve by Incident type for ' \
                                     '' \
                                     'last 2 Quarters'
        assert api_response[0].version == 4

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == '/reports'
        assert responses.calls[0].request.host == 'localhost'
        assert responses.calls[0].request.scheme == 'http'

    run()
    assert_reset()


def test_indicators_search():
    '''Testing search for indicator.'''

    @responses.activate
    def run():
        body = r'''
        {
        "iocObjects": [{
            "id": "4737",
            "version": 1,
            "modified": "2019-07-14T16:54:02.719044+03:00",
            "account": "",
            "timestamp": "2019-07-14T16:54:02.718422+03:00",
            "indicator_type": "IP",
            "value": "92.63.197.153",
            "source": "Recorded Future",
            "investigationIDs": ["1750"],
            "lastSeen": "2019-07-14T16:54:02.718378+03:00",
            "firstSeen": "2019-07-14T16:54:02.718378+03:00",
            "lastSeenEntryID": "API",
            "firstSeenEntryID": "API",
            "score": 3,
            "manualScore": true,
            "setBy": "DBotWeak",
            "manualSetTime": "0001-01-01T00:00:00Z",
            "insightCache": null,
            "calculatedTime": "2019-07-14T16:54:02.718378+03:00",
            "lastReputationRun": "0001-01-01T00:00:00Z",
            "comment": "From Recorded Future risk list, Score - 89",
            "manuallyEditedFields": null
        }],
        "total": 1
    }
    '''

        responses.add('POST', '/indicators/search',
                      body=body,
                      status=200,
                      content_type='application/json')
        api_instance = demisto_client.configure(base_url=host, api_key=api_key, debug=False)
        indicator_filter = demisto_client.demisto_api.IndicatorFilter()  # IndicatorFilter |  (optional)
        indicator_filter.query = 'value:92.63.197.153'
        api_response = api_instance.indicators_search(indicator_filter=indicator_filter)

        assert api_response.ioc_objects[0].get('comment') == 'From Recorded Future risk list, Score - 89'
        # assert api_response.type == 'Unclassified'
        # assert api_response.owner == 'Admin'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == '/indicators/search'
        assert responses.calls[0].request.host == 'localhost'
        assert responses.calls[0].request.scheme == 'http'

    run()
    assert_reset()


def test_export_entry():
    '''Testing export entry artifact.'''

    @responses.activate
    def run():
        body = "entry_artifact_6@1770.md"
        responses.add('POST', '/entry/exportArtifact',
                      body=body,
                      status=200,
                      content_type='application/json')
        api_instance = demisto_client.configure(base_url=host, api_key=api_key, debug=False)
        download_entry = demisto_client.demisto_api.DownloadEntry()  # DownloadEntry |  (optional)

        download_entry.id = '6@1770'
        download_entry.investigation_id = '1770'

        api_result = api_instance.entry_export_artifact(download_entry=download_entry)

        assert api_result == 'entry_artifact_6@1770.md'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == '/entry/exportArtifact'
        assert responses.calls[0].request.host == 'localhost'
        assert responses.calls[0].request.scheme == 'http'

    run()
    assert_reset()


def test_generic_request():
    '''Testing generic requst.'''

    @responses.activate
    def run():
        responses.add('POST', '/test',
                      body="all good",
                      status=200,
                      content_type='text/plain')
        api_instance = demisto_client.configure(base_url=host, api_key=api_key, debug=False)
        (res, code, headers) = api_instance.generic_request('/test', 'POST', body="this is a test",
                                                            content_type='text/plain', accept='text/plain')

        assert res == 'all good'
        assert code == 200

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == '/test'
        assert responses.calls[0].request.host == 'localhost'
        assert responses.calls[0].request.scheme == 'http'

    run()
    assert_reset()


def test_import_layout(mocker):
    """
    Given:
        - Path for a layoutscontainer.
    When
        - Using client.import_layout() to upload a new layout.
    Then
        - The layout is being uploaded and getting back the layout metadata.
    """
    client = demisto_client.configure(base_url=host, api_key=api_key, debug=False,
                                      verify_ssl=False)
    mocker.patch.object(client, 'import_layout_with_http_info', return_value={'test': 'test'})
    res = client.import_layout('tests_data/layoutscontainer-test.json')
    assert res.get('test') == 'test'


def test_import_layout_with_http_info_with_knowing_server_version(mocker):
    """
    Given:
        - path for a layoutscontainer.
    When
        - Succeeding in getting demisto version using 'get_layouts_url_for_demisto_version' function
    Then
        - The layout is being uploaded and getting back the layout metadata.
    """
    client = demisto_client.configure(base_url=host, api_key=api_key, debug=False,
                                      verify_ssl=False)
    mocker.patch.object(client.api_client, 'call_api', side_effect=[("{'demistoVersion': '6.0.0'}", 200, {'Content-type': 'application/json'}),  {'test': 'test'}])
    res = client.import_layout('tests_data/layoutscontainer-test.json')
    assert res.get('test') == 'test'


def test_import_layout_with_http_info_without_knowing_server_version(mocker):
    """
    Given:
        - Path for a layoutscontainer.
    When
        - Not knowing demisto version, and working with 6.0.0 or higher
    Then
        - The layout is being uploaded and getting back the layout metadata.
    """
    client = demisto_client.configure(base_url=host, api_key=api_key, debug=False,
                                      verify_ssl=False)
    mocker.patch.object(client.api_client, 'call_api', side_effect=[("{'demistoVersion': '6.0.0'}", 404, {'Content-type': 'application/json'}),  {'test': 'test'}])
    res = client.import_layout('tests_data/layoutscontainer-test.json')
    assert res.get('test') == 'test'


def test_import_layout_with_http_info_with_old_layout_format(mocker):
    """
    Given:
        - Path for a layout
    When
        - Working with 5.0.0 and uploading a layout(the old version)
    Then
        - The layout is being uploaded and getting back the layout metadata.
    """
    client = demisto_client.configure(base_url=host, api_key=api_key, debug=False,
                                      verify_ssl=False)

    mocker.patch.object(client.api_client, 'call_api', side_effect=[("{'demistoVersion': '5.0.0'}", 200, {'Content-type': 'application/json'}),  {'test': 'test'}])
    res = client.import_layout('tests_data/layout-details-test-V2.json')
    assert res.get('test') == 'test'


class TestFailedGenericRequestNoEnv(unittest.TestCase):

    def test_generic_request(self):
        """
        Given:
        - Request which should result in an ApiException
        When:
        - No environment variable has been set
        Then:
        - Return ApiException without the headers in the error
        """
        from demisto_client.demisto_api.rest import ApiException

        @responses.activate
        def run():
            responses.add('POST', '/test',
                          body="Not good",
                          status=400,
                          content_type='text/plain')
            api_instance = demisto_client.configure(base_url=host, api_key=api_key, debug=False)

            with self.assertRaises(ApiException) as context:
                (_, _, _) = api_instance.generic_request('/test', 'POST',
                                                                    body="this is a test",
                                                                    content_type='text/plain',
                                                                    accept='text/plain')
            self.assertTrue('HTTP response body' in str(context.exception))
            self.assertFalse('HTTP response headers' in str(context.exception))
            assert len(responses.calls) == 1
            assert responses.calls[0].request.url == '/test'
            assert responses.calls[0].request.host == 'localhost'
            assert responses.calls[0].request.scheme == 'http'

        run()
        assert_reset()


class TestFailedGenericRequestWithEnv(unittest.TestCase):

    def test_generic_request(self):
        """
        Given:
        - Request which should result in an ApiException
        When:
        - Environment variable DEMISTO_EXCEPTION_HEADER_LOGGING has been set to true
        Then:
        - Return ApiException with the headers in the error
        """
        import sys
        # Error should be the same in both Py2 and Py3, but Py2 does not support unittest mock in
        # the same way
        if sys.version_info[0] > 2:
            import os
            from demisto_client.demisto_api.rest import ApiException
            from unittest import mock

            @mock.patch.dict(os.environ, {"DEMISTO_EXCEPTION_HEADER_LOGGING": "true"})
            @responses.activate
            def run():
                responses.add('POST', '/test',
                              body="Not good",
                              status=400,
                              content_type='text/plain')
                api_instance = demisto_client.configure(base_url=host, api_key=api_key, debug=False)

                with self.assertRaises(ApiException) as context:
                    (_, _, _) = api_instance.generic_request('/test', 'POST',
                                                             body="this is a test",
                                                             content_type='text/plain',
                                                             accept='text/plain')
                self.assertTrue('HTTP response body' in str(context.exception))
                self.assertTrue('HTTP response headers' in str(context.exception))
                assert len(responses.calls) == 1
                assert responses.calls[0].request.url == '/test'
                assert responses.calls[0].request.host == 'localhost'
                assert responses.calls[0].request.scheme == 'http'
        else:
            def run():
                assert 1 == 1
        run()
        assert_reset()


class TestWithProxyBasicAuthentication(unittest.TestCase):

    def test_generic_request(self):
        """
        Given:
        - Request which use proxy authentication
        When:
        - Environment variable HTTP_PROXY and HTTPS_PROXY which contains a username and password with special characters
        Then:
        - Ensure the request made to the correct url via correct proxy username and password. Special character should be decoded.
        """
        import sys
        # Error should be the same in both Py2 and Py3, but Py2 does not support unittest mock in
        # the same way
        if sys.version_info[0] > 2:
            from unittest import mock

            @mock.patch.dict(os.environ, {"HTTP_PROXY": "http://user1:pass%21%23%24%25%5E@localhost:8080"})
            @mock.patch.dict(os.environ, {"HTTPS_PROXY": "http://user1:pass%21%23%24%25%5E@localhost:8080"})
            @responses.activate
            def run():
                responses.add('POST', 'http://localhost:8080/test',
                              body="Good",
                              status=200,
                              content_type='text/plain')
                api_instance = demisto_client.configure(base_url=host, api_key=api_key, debug=False)

                api_instance.generic_request('/test', 'POST',
                                            body="this is a test",
                                            content_type='text/plain',
                                            accept='text/plain')

                assert len(responses.calls) == 1
                assert responses.calls[0].request.url == 'http://localhost:8080/test'
                assert responses.calls[0].request.host == 'localhost'
                assert responses.calls[0].request.scheme == 'http'
                assert api_instance.api_client.configuration.proxy_auth == 'user1:pass!#$%^'
                
        else:
            def run():
                assert 1 == 1
        run()
        assert_reset()


def test_import_incidentfields(mocker):
    """
    Given:
        A path for a incidentfield.
    When:
        Importing incidentfields with partial errors.
    Then:
        Make sure the partial error is returned.
    """

    api_instance = demisto_client.configure(base_url=host, api_key=api_key, debug=False)

    raw_http_response = urllib3.response.HTTPResponse(body=b'{"incidentFields":[{"id":"evidence_description"}],'
                                                           b'"error":"Partial Error Description"}\n', status=200)
    mocker.patch.object(rest.RESTClientObject, 'POST', return_value=raw_http_response)
    with tempfile.NamedTemporaryFile() as tmp:
        res = api_instance.import_incident_fields(tmp.name)
    if isinstance(res, dict):
        assert res.get('error') == 'Partial Error Description'
    else:
        assert hasattr(res, 'error')
        assert res.error == 'Partial Error Description'


class TestConfigureClient:

    CONFIGURE_TEST_PARAMS = [
        (
            'api_key', 'username', {"header1": "value1", "header2": "value2"}, False
        ),
        (
            None, 'username', {"header1": "value1"}, True
        ),
        (
            'api_key', None, None, False
        ),
        (
            None, None, None, False
        ),
    ]

    CONFIGURE_TEST_PARAMS_ENV_VARIABLE = [
        (
            'api_key', 'username', "header1=value1,header2=value2", False
        ),
        (
            None, 'username', "header1=value1", True
        ),
        (
            'api_key', None, None, False
        ),
        (
            None, None, None, False
        ),
    ]

    @staticmethod
    def getenv_decorator(username=None, _api_key=None, additional_headers=None):
        def getenv_side_effect(parameter):
            if parameter == 'DEMISTO_API_KEY':
                return _api_key
            elif parameter == 'DEMISTO_USERNAME':
                return username
            elif parameter == 'DEMISTO_HTTP_HEADERS':
                return additional_headers
            return None

        return getenv_side_effect

    @staticmethod
    def configure_client(_api_key=None, username=None, additional_headers=None):
        if not (_api_key or os.getenv('DEMISTO_API_KEY')) and not (username or os.getenv('DEMISTO_USERNAME')):
            with pytest.raises(ValueError):
                demisto_client.configure(
                    base_url=host, api_key=_api_key, username=username, additional_headers=additional_headers
                )
        else:
            return demisto_client.configure(
                base_url=host, api_key=_api_key, username=username, additional_headers=additional_headers
            )

    def validate_additional_headers(
        self, api_instance, http_request_mocker, num_of_http_requests_mock, expected_additional_headers
    ):
        if not expected_additional_headers.items() <= api_instance.api_client.default_headers.items():
            return False

        self.run_http_request(api_instance, num_of_http_requests_mock=num_of_http_requests_mock)

        for i in range(len(http_request_mocker.call_args_list)):
            if not expected_additional_headers.items() <= http_request_mocker.call_args_list[i].kwargs['headers'].items():
                return False

        return True

    @staticmethod
    def run_http_request(api_instance, num_of_http_requests_mock):
        for i in range(num_of_http_requests_mock):
            api_instance.generic_request(path='/about', method='GET')

    @pytest.mark.parametrize(
        "_api_key, username, additional_headers, should_login_called",
        CONFIGURE_TEST_PARAMS
    )
    def test_configure_client_no_env_vars(self, mocker, _api_key, username, additional_headers, should_login_called):
        """
        Given:
            Case A: api key, username and additional headers were provided
            Case B: username and additional headers were provided
            Case C: only api key was provided
            Case D: neither of api key / username was provided

        When:
            configuring the client

        Then:
            Case A: make sure login was not called, authentication is via api key and
                    additional headers were sent in each request
            Case B: make sure login was called, authentication is via username/password and
                    additional headers were sent in each request
            Case C: make sure login was not called and authentication is via api key
            Case D: make sure an exception is raised
        """
        num_of_http_requests_mock = 5
        http_request_mocker = get_login_mocker(mocker, num_of_http_requests_mock=num_of_http_requests_mock)

        api_instance = self.configure_client(
            _api_key=_api_key, username=username, additional_headers=additional_headers
        )

        assert http_request_mocker.called == should_login_called

        if api_instance and additional_headers is not None:
            assert self.validate_additional_headers(
                api_instance,
                http_request_mocker,
                num_of_http_requests_mock=num_of_http_requests_mock,
                expected_additional_headers=additional_headers
            )

    @pytest.mark.parametrize(
        "_api_key, username, additional_headers, should_login_called",
        CONFIGURE_TEST_PARAMS_ENV_VARIABLE
    )
    def test_configure_client_env_vars(self, mocker, _api_key, username, additional_headers, should_login_called):
        """
        Given:
            Case A: api key, username and additional headers were provided through environment variables
            Case B: username and additional headers were provided through environment variables
            Case C: only api key was provided through environment variable
            Case D: neither of api key / username was provided at all

        When:
            configuring the client

        Then:
            Case A: make sure login was not called, authentication is via api key and
                    additional headers were sent in each request
            Case B: make sure login was called, authentication is via username/password, and
                    additional headers were sent in each request
            Case C: make sure login was not called and authentication is via api key
            Case D: make sure an exception is raised
        """
        num_of_http_requests_mock = 5

        http_request_mocker = get_login_mocker(mocker, num_of_http_requests_mock=num_of_http_requests_mock)
        mocker.patch.object(
            os,
            'getenv',
            side_effect=self.getenv_decorator(
                username=username, _api_key=_api_key, additional_headers=additional_headers
            )
        )

        api_instance = self.configure_client()
        assert http_request_mocker.called == should_login_called

        if api_instance and additional_headers is not None:
            expected_additional_headers = dict(header.split('=') for header in additional_headers.split(','))

            assert self.validate_additional_headers(
                api_instance,
                http_request_mocker,
                num_of_http_requests_mock=num_of_http_requests_mock,
                expected_additional_headers=expected_additional_headers
            )

    @pytest.mark.parametrize(
        "invalid_additional_headers",
        [
            "header1:value1,header2:value2",
            "header1,value1,header2,value2",
            "header1=value1,header2,value2",
            "header1=value1,header2value2",
            "header1=value1header2=value2",
            "test",
            "{header1:value1,header2:value2}",
            "test=test,",
            "test=test,test2=",
            "test=test, test2=a",
            "arg=arg,  c=d",
            "arg-arg,  c=d",
            "1=2,3=",
            "name=john,",
            "name=john age=42",
            "bar=",
            "name,",
            "header1=value1 header2=value2",
            "!=1 d",
            "!=1\nd"
        ]
    )
    def test_configure_client_invalid_additional_headers_form_env_var(self, mocker, invalid_additional_headers):
        """
        Given:
            invalid form of http headers

        When:
            configuring the client

        Then:
            make sure an exception is raised saying the format for invalid_additional_headers is invalid
        """
        mocker.patch.object(
            os,
            'getenv',
            side_effect=self.getenv_decorator(additional_headers=invalid_additional_headers)
        )

        with pytest.raises(ValueError) as exc:
            demisto_client.configure(base_url=host, api_key=api_key)

        assert exc.value.args[0] == f'{invalid_additional_headers} has invalid format, must be in the format ' \
                                    f'of header1=value1,header2=value2,...headerN=valueN'

    @pytest.mark.parametrize(
        "valid_additional_headers, expected_headers_as_dict",
        [
            (
                "header1=value1,header2=value2",
                {'header1': 'value1', 'header2': 'value2'}
            ),
            (
                "header1=value1",
                {'header1': 'value1'}
            ),
            (
                "blabla=1!,headers=2@",
                {'blabla': '1!', 'headers': '2@'}
            ),
            (
                "header1=with space,header2=another space",
                {'header1': 'with space', 'header2': 'another space'}
            ),
            (
                "header-1=value-1,header-2=value-2",
                {'header-1': 'value-1', 'header-2': 'value-2'}
            ),
            (
                "header1=header1,header2=header2,header3=header3,header4=header4,header5=header5",
                {'header1': 'header1', 'header2': 'header2', 'header3': 'header3', 'header4': 'header4', 'header5': 'header5'}
            ),
            (
                "PROXY=@$%#!djaj,PROXY2=[123]#%",
                {'PROXY': '@$%#!djaj', 'PROXY2': '[123]#%'}
            ),
            (
                "Proxy-Authorization=#$32dll1223--ds,header2=dkkfff",
                {'Proxy-Authorization': '#$32dll1223--ds', 'header2': 'dkkfff'}
            ),
            (
                "Content-type=123",
                {'Content-type': '123'}
            ),
            (
                "  ",
                {}
            ),
            (
                "",
                {}
            ),
        ]
    )
    def test_configure_client_valid_additional_headers_form_env_var(
        self, mocker, valid_additional_headers, expected_headers_as_dict
    ):
        """
        Given:
            valid form of http headers

        When:
            configuring the client

        Then:
            make sure the client is configured correctly, no exception is raised and
            headers were added to default headers for every http request
        """
        mocker.patch.object(
            os,
            'getenv',
            side_effect=self.getenv_decorator(additional_headers=valid_additional_headers)
        )

        client = demisto_client.configure(base_url=host, api_key=api_key)
        assert expected_headers_as_dict.items() <= client.api_client.default_headers.items()