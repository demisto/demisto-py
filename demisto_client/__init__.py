import demisto_client.demisto_api as demisto_api
import six

# import ApiClient
from demisto_client.demisto_api import ApiClient
from demisto_client.demisto_api.configuration import Configuration


def configure(hostname, api_key=None, username=None, password=None, verify_ssl=True, proxy=None,
              debug=False):
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


def to_good_dict(o):
    """Returns the model properties as a dict"""
    result = {}
    o_map = o.attribute_map

    for attr, _ in six.iteritems(o.swagger_types):
        value = getattr(o, attr)
        if isinstance(value, list):
            result[o_map[attr]] = list(map(
                lambda x: to_good_dict(x) if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result[o_map[attr]] = to_good_dict(value)
        elif isinstance(value, dict):
            result[o_map[attr]] = dict(map(
                lambda item: (item[0], to_good_dict(item[1]))
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result[o_map[attr]] = value

    return result
