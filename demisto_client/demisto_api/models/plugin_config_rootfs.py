# coding: utf-8

"""
    Cortex XSOAR API

    This is the public REST API to integrate with the Cortex XSOAR server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Cortex XSOAR web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Cortex XSOAR REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Cortex XSOAR server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Cortex XSOAR has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Cortex XSOAR will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PluginConfigRootfs(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'diff_ids': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'diff_ids': 'diff_ids',
        'type': 'type'
    }

    def __init__(self, diff_ids=None, type=None):  # noqa: E501
        """PluginConfigRootfs - a model defined in Swagger"""  # noqa: E501

        self._diff_ids = None
        self._type = None
        self.discriminator = None

        if diff_ids is not None:
            self.diff_ids = diff_ids
        if type is not None:
            self.type = type

    @property
    def diff_ids(self):
        """Gets the diff_ids of this PluginConfigRootfs.  # noqa: E501

        diff ids  # noqa: E501

        :return: The diff_ids of this PluginConfigRootfs.  # noqa: E501
        :rtype: list[str]
        """
        return self._diff_ids

    @diff_ids.setter
    def diff_ids(self, diff_ids):
        """Sets the diff_ids of this PluginConfigRootfs.

        diff ids  # noqa: E501

        :param diff_ids: The diff_ids of this PluginConfigRootfs.  # noqa: E501
        :type: list[str]
        """

        self._diff_ids = diff_ids

    @property
    def type(self):
        """Gets the type of this PluginConfigRootfs.  # noqa: E501

        type  # noqa: E501

        :return: The type of this PluginConfigRootfs.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PluginConfigRootfs.

        type  # noqa: E501

        :param type: The type of this PluginConfigRootfs.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PluginConfigRootfs, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PluginConfigRootfs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
