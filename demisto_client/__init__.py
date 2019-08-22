import demisto_client.demisto_api as demisto_api

# import ApiClient
from demisto_client.demisto_api import ApiClient
from demisto_client.demisto_api.configuration import Configuration


def configure(hostname, api_key=None, username=None, password=None, verify_ssl=True, proxy=None, debug=False):
    configuration = Configuration()
    configuration.api_key['Authorization'] = api_key
    configuration.host = hostname
    configuration.username = username
    configuration.password = password
    configuration.verify_ssl = verify_ssl
    configuration.proxy = proxy
    configuration.debug = debug
    api_instance = demisto_api.DefaultApi(ApiClient(configuration))
    return api_instance
