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

from demisto_client.demisto_api.models.config_data_type import ConfigDataType  # noqa: F401,E501


class ConfigField(object):
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
        'default_value': 'str',
        'display': 'str',
        'display_password': 'str',
        'hidden': 'bool',
        'hidden_password': 'bool',
        'hidden_username': 'bool',
        'info': 'str',
        'name': 'str',
        'options': 'list[str]',
        'required': 'bool',
        'type': 'ConfigDataType'
    }

    attribute_map = {
        'default_value': 'defaultValue',
        'display': 'display',
        'display_password': 'displayPassword',
        'hidden': 'hidden',
        'hidden_password': 'hiddenPassword',
        'hidden_username': 'hiddenUsername',
        'info': 'info',
        'name': 'name',
        'options': 'options',
        'required': 'required',
        'type': 'type'
    }

    def __init__(self, default_value=None, display=None, display_password=None, hidden=None, hidden_password=None, hidden_username=None, info=None, name=None, options=None, required=None, type=None):  # noqa: E501
        """ConfigField - a model defined in Swagger"""  # noqa: E501

        self._default_value = None
        self._display = None
        self._display_password = None
        self._hidden = None
        self._hidden_password = None
        self._hidden_username = None
        self._info = None
        self._name = None
        self._options = None
        self._required = None
        self._type = None
        self.discriminator = None

        if default_value is not None:
            self.default_value = default_value
        if display is not None:
            self.display = display
        if display_password is not None:
            self.display_password = display_password
        if hidden is not None:
            self.hidden = hidden
        if hidden_password is not None:
            self.hidden_password = hidden_password
        if hidden_username is not None:
            self.hidden_username = hidden_username
        if info is not None:
            self.info = info
        if name is not None:
            self.name = name
        if options is not None:
            self.options = options
        if required is not None:
            self.required = required
        if type is not None:
            self.type = type

    @property
    def default_value(self):
        """Gets the default_value of this ConfigField.  # noqa: E501


        :return: The default_value of this ConfigField.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this ConfigField.


        :param default_value: The default_value of this ConfigField.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def display(self):
        """Gets the display of this ConfigField.  # noqa: E501


        :return: The display of this ConfigField.  # noqa: E501
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this ConfigField.


        :param display: The display of this ConfigField.  # noqa: E501
        :type: str
        """

        self._display = display

    @property
    def display_password(self):
        """Gets the display_password of this ConfigField.  # noqa: E501


        :return: The display_password of this ConfigField.  # noqa: E501
        :rtype: str
        """
        return self._display_password

    @display_password.setter
    def display_password(self, display_password):
        """Sets the display_password of this ConfigField.


        :param display_password: The display_password of this ConfigField.  # noqa: E501
        :type: str
        """

        self._display_password = display_password

    @property
    def hidden(self):
        """Gets the hidden of this ConfigField.  # noqa: E501


        :return: The hidden of this ConfigField.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ConfigField.


        :param hidden: The hidden of this ConfigField.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def hidden_password(self):
        """Gets the hidden_password of this ConfigField.  # noqa: E501


        :return: The hidden_password of this ConfigField.  # noqa: E501
        :rtype: bool
        """
        return self._hidden_password

    @hidden_password.setter
    def hidden_password(self, hidden_password):
        """Sets the hidden_password of this ConfigField.


        :param hidden_password: The hidden_password of this ConfigField.  # noqa: E501
        :type: bool
        """

        self._hidden_password = hidden_password

    @property
    def hidden_username(self):
        """Gets the hidden_username of this ConfigField.  # noqa: E501


        :return: The hidden_username of this ConfigField.  # noqa: E501
        :rtype: bool
        """
        return self._hidden_username

    @hidden_username.setter
    def hidden_username(self, hidden_username):
        """Sets the hidden_username of this ConfigField.


        :param hidden_username: The hidden_username of this ConfigField.  # noqa: E501
        :type: bool
        """

        self._hidden_username = hidden_username

    @property
    def info(self):
        """Gets the info of this ConfigField.  # noqa: E501


        :return: The info of this ConfigField.  # noqa: E501
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this ConfigField.


        :param info: The info of this ConfigField.  # noqa: E501
        :type: str
        """

        self._info = info

    @property
    def name(self):
        """Gets the name of this ConfigField.  # noqa: E501


        :return: The name of this ConfigField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigField.


        :param name: The name of this ConfigField.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def options(self):
        """Gets the options of this ConfigField.  # noqa: E501


        :return: The options of this ConfigField.  # noqa: E501
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ConfigField.


        :param options: The options of this ConfigField.  # noqa: E501
        :type: list[str]
        """

        self._options = options

    @property
    def required(self):
        """Gets the required of this ConfigField.  # noqa: E501


        :return: The required of this ConfigField.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ConfigField.


        :param required: The required of this ConfigField.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def type(self):
        """Gets the type of this ConfigField.  # noqa: E501


        :return: The type of this ConfigField.  # noqa: E501
        :rtype: ConfigDataType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConfigField.


        :param type: The type of this ConfigField.  # noqa: E501
        :type: ConfigDataType
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
        if issubclass(ConfigField, dict):
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
        if not isinstance(other, ConfigField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
