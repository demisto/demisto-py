import unittest

from urllib3_mock import Responses
import demisto_client
from datetime import datetime
import json
responses = Responses('requests.packages.urllib3')

api_key = 'sample_api_key'
host = 'http://localhost:8080'


def assert_reset():
    assert len(responses._urls) == 0
    assert len(responses.calls) == 0


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
