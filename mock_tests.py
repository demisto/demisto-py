from urllib3_mock import Responses
import demisto_client

responses = Responses('requests.packages.urllib3')

api_key = 'sample_api_key'
host = 'http://localhost:8080'


@responses.activate
def test_get_docker_images():
    body = '{ "images": [{"id": "aae7b8aaba8c", "repository": ' \
           '"openapitools/openapi-generator-cli", "tag": "latest", "createdSince": "3 days ago", ' \
           '"createdAt": "2019-08-19 13:34:22 +0300 IDT", "size": "131MB" }]}'
    responses.add('GET', '/settings/docker-images',
                  body=body,
                  status=200,
                  content_type='application/json')

    # create an instance of the API class
    api_instance = demisto_client.configure(hostname=host, api_key=api_key)
    api_response = api_instance.get_docker_images()

    assert api_response.images[0].created_at == '2019-08-19 13:34:22 +0300 IDT'
    assert api_response.images[0].id == 'aae7b8aaba8c'
    assert api_response.images[0].repository == 'openapitools/openapi-generator-cli'

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == '/settings/docker-images'
    assert responses.calls[0].request.host == 'localhost'
    assert responses.calls[0].request.scheme == 'http'


@responses.activate
def test_create_incident():
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
    api_instance = demisto_client.configure(hostname=host, api_key=api_key)
    create_incident_request = demisto_client.demisto_api.CreateIncidentRequest()
    create_incident_request.name = 'Test Incident'
    create_incident_request.type = 'Unclassified'
    create_incident_request.owner = 'Admin'
    api_response = api_instance.create_incident(create_incident_request=create_incident_request)

    print(api_response)

    assert api_response.name == 'Test Incident'
    assert api_response.type == 'Unclassified'
    assert api_response.owner == 'Admin'

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == '/incident'
    assert responses.calls[0].request.host == 'localhost'
    assert responses.calls[0].request.scheme == 'http'
