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


class WhitelistedIndicator(object):
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
        'highlight': 'dict(str, list[str])',
        'id': 'str',
        'locked': 'bool',
        'modified': 'datetime',
        'numeric_id': 'int',
        'primary_term': 'int',
        'reason': 'str',
        'reputations': 'list[str]',
        'sequence_number': 'int',
        'sort_values': 'list[str]',
        'type': 'str',
        'user': 'str',
        'value': 'str',
        'version': 'int',
        'whitelist_time': 'datetime'
    }

    attribute_map = {
        'highlight': 'highlight',
        'id': 'id',
        'locked': 'locked',
        'modified': 'modified',
        'numeric_id': 'numericId',
        'primary_term': 'primaryTerm',
        'reason': 'reason',
        'reputations': 'reputations',
        'sequence_number': 'sequenceNumber',
        'sort_values': 'sortValues',
        'type': 'type',
        'user': 'user',
        'value': 'value',
        'version': 'version',
        'whitelist_time': 'whitelistTime'
    }

    def __init__(self, highlight=None, id=None, locked=None, modified=None, numeric_id=None, primary_term=None, reason=None, reputations=None, sequence_number=None, sort_values=None, type=None, user=None, value=None, version=None, whitelist_time=None):  # noqa: E501
        """WhitelistedIndicator - a model defined in Swagger"""  # noqa: E501

        self._highlight = None
        self._id = None
        self._locked = None
        self._modified = None
        self._numeric_id = None
        self._primary_term = None
        self._reason = None
        self._reputations = None
        self._sequence_number = None
        self._sort_values = None
        self._type = None
        self._user = None
        self._value = None
        self._version = None
        self._whitelist_time = None
        self.discriminator = None

        if highlight is not None:
            self.highlight = highlight
        if id is not None:
            self.id = id
        if locked is not None:
            self.locked = locked
        if modified is not None:
            self.modified = modified
        if numeric_id is not None:
            self.numeric_id = numeric_id
        if primary_term is not None:
            self.primary_term = primary_term
        if reason is not None:
            self.reason = reason
        if reputations is not None:
            self.reputations = reputations
        if sequence_number is not None:
            self.sequence_number = sequence_number
        if sort_values is not None:
            self.sort_values = sort_values
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user
        if value is not None:
            self.value = value
        if version is not None:
            self.version = version
        if whitelist_time is not None:
            self.whitelist_time = whitelist_time

    @property
    def highlight(self):
        """Gets the highlight of this WhitelistedIndicator.  # noqa: E501


        :return: The highlight of this WhitelistedIndicator.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._highlight

    @highlight.setter
    def highlight(self, highlight):
        """Sets the highlight of this WhitelistedIndicator.


        :param highlight: The highlight of this WhitelistedIndicator.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._highlight = highlight

    @property
    def id(self):
        """Gets the id of this WhitelistedIndicator.  # noqa: E501


        :return: The id of this WhitelistedIndicator.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WhitelistedIndicator.


        :param id: The id of this WhitelistedIndicator.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def locked(self):
        """Gets the locked of this WhitelistedIndicator.  # noqa: E501


        :return: The locked of this WhitelistedIndicator.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this WhitelistedIndicator.


        :param locked: The locked of this WhitelistedIndicator.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def modified(self):
        """Gets the modified of this WhitelistedIndicator.  # noqa: E501


        :return: The modified of this WhitelistedIndicator.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this WhitelistedIndicator.


        :param modified: The modified of this WhitelistedIndicator.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def numeric_id(self):
        """Gets the numeric_id of this WhitelistedIndicator.  # noqa: E501


        :return: The numeric_id of this WhitelistedIndicator.  # noqa: E501
        :rtype: int
        """
        return self._numeric_id

    @numeric_id.setter
    def numeric_id(self, numeric_id):
        """Sets the numeric_id of this WhitelistedIndicator.


        :param numeric_id: The numeric_id of this WhitelistedIndicator.  # noqa: E501
        :type: int
        """

        self._numeric_id = numeric_id

    @property
    def primary_term(self):
        """Gets the primary_term of this WhitelistedIndicator.  # noqa: E501


        :return: The primary_term of this WhitelistedIndicator.  # noqa: E501
        :rtype: int
        """
        return self._primary_term

    @primary_term.setter
    def primary_term(self, primary_term):
        """Sets the primary_term of this WhitelistedIndicator.


        :param primary_term: The primary_term of this WhitelistedIndicator.  # noqa: E501
        :type: int
        """

        self._primary_term = primary_term

    @property
    def reason(self):
        """Gets the reason of this WhitelistedIndicator.  # noqa: E501


        :return: The reason of this WhitelistedIndicator.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this WhitelistedIndicator.


        :param reason: The reason of this WhitelistedIndicator.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def reputations(self):
        """Gets the reputations of this WhitelistedIndicator.  # noqa: E501


        :return: The reputations of this WhitelistedIndicator.  # noqa: E501
        :rtype: list[str]
        """
        return self._reputations

    @reputations.setter
    def reputations(self, reputations):
        """Sets the reputations of this WhitelistedIndicator.


        :param reputations: The reputations of this WhitelistedIndicator.  # noqa: E501
        :type: list[str]
        """

        self._reputations = reputations

    @property
    def sequence_number(self):
        """Gets the sequence_number of this WhitelistedIndicator.  # noqa: E501


        :return: The sequence_number of this WhitelistedIndicator.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this WhitelistedIndicator.


        :param sequence_number: The sequence_number of this WhitelistedIndicator.  # noqa: E501
        :type: int
        """

        self._sequence_number = sequence_number

    @property
    def sort_values(self):
        """Gets the sort_values of this WhitelistedIndicator.  # noqa: E501


        :return: The sort_values of this WhitelistedIndicator.  # noqa: E501
        :rtype: list[str]
        """
        return self._sort_values

    @sort_values.setter
    def sort_values(self, sort_values):
        """Sets the sort_values of this WhitelistedIndicator.


        :param sort_values: The sort_values of this WhitelistedIndicator.  # noqa: E501
        :type: list[str]
        """

        self._sort_values = sort_values

    @property
    def type(self):
        """Gets the type of this WhitelistedIndicator.  # noqa: E501


        :return: The type of this WhitelistedIndicator.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WhitelistedIndicator.


        :param type: The type of this WhitelistedIndicator.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def user(self):
        """Gets the user of this WhitelistedIndicator.  # noqa: E501


        :return: The user of this WhitelistedIndicator.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this WhitelistedIndicator.


        :param user: The user of this WhitelistedIndicator.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def value(self):
        """Gets the value of this WhitelistedIndicator.  # noqa: E501


        :return: The value of this WhitelistedIndicator.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this WhitelistedIndicator.


        :param value: The value of this WhitelistedIndicator.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def version(self):
        """Gets the version of this WhitelistedIndicator.  # noqa: E501


        :return: The version of this WhitelistedIndicator.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WhitelistedIndicator.


        :param version: The version of this WhitelistedIndicator.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def whitelist_time(self):
        """Gets the whitelist_time of this WhitelistedIndicator.  # noqa: E501


        :return: The whitelist_time of this WhitelistedIndicator.  # noqa: E501
        :rtype: datetime
        """
        return self._whitelist_time

    @whitelist_time.setter
    def whitelist_time(self, whitelist_time):
        """Sets the whitelist_time of this WhitelistedIndicator.


        :param whitelist_time: The whitelist_time of this WhitelistedIndicator.  # noqa: E501
        :type: datetime
        """

        self._whitelist_time = whitelist_time

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
        if issubclass(WhitelistedIndicator, dict):
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
        if not isinstance(other, WhitelistedIndicator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
