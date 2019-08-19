import demisto_client.demisto_api as demisto_api


def configure():
    return demisto_api.DefaultApi()
