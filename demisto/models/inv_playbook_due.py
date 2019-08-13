# coding: utf-8

"""
    Demisto API

    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InvPlaybookDue(object):
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
        '_date': 'datetime',
        'in_task_id': 'str',
        'inv_id': 'str',
        'version': 'int'
    }

    attribute_map = {
        '_date': 'date',
        'in_task_id': 'inTaskID',
        'inv_id': 'invId',
        'version': 'version'
    }

    def __init__(self, _date=None, in_task_id=None, inv_id=None, version=None):  # noqa: E501
        """InvPlaybookDue - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._in_task_id = None
        self._inv_id = None
        self._version = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if in_task_id is not None:
            self.in_task_id = in_task_id
        if inv_id is not None:
            self.inv_id = inv_id
        if version is not None:
            self.version = version

    @property
    def _date(self):
        """Gets the _date of this InvPlaybookDue.  # noqa: E501


        :return: The _date of this InvPlaybookDue.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this InvPlaybookDue.


        :param _date: The _date of this InvPlaybookDue.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def in_task_id(self):
        """Gets the in_task_id of this InvPlaybookDue.  # noqa: E501


        :return: The in_task_id of this InvPlaybookDue.  # noqa: E501
        :rtype: str
        """
        return self._in_task_id

    @in_task_id.setter
    def in_task_id(self, in_task_id):
        """Sets the in_task_id of this InvPlaybookDue.


        :param in_task_id: The in_task_id of this InvPlaybookDue.  # noqa: E501
        :type: str
        """

        self._in_task_id = in_task_id

    @property
    def inv_id(self):
        """Gets the inv_id of this InvPlaybookDue.  # noqa: E501


        :return: The inv_id of this InvPlaybookDue.  # noqa: E501
        :rtype: str
        """
        return self._inv_id

    @inv_id.setter
    def inv_id(self, inv_id):
        """Sets the inv_id of this InvPlaybookDue.


        :param inv_id: The inv_id of this InvPlaybookDue.  # noqa: E501
        :type: str
        """

        self._inv_id = inv_id

    @property
    def version(self):
        """Gets the version of this InvPlaybookDue.  # noqa: E501


        :return: The version of this InvPlaybookDue.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InvPlaybookDue.


        :param version: The version of this InvPlaybookDue.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(InvPlaybookDue, dict):
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
        if not isinstance(other, InvPlaybookDue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
