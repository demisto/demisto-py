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

from demisto_client.demisto_api.models.widget import Widget  # noqa: F401,E501


class WidgetCell(object):
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
        'force_range': 'bool',
        'h': 'int',
        'i': 'str',
        'id': 'str',
        'w': 'int',
        'widget': 'Widget',
        'x': 'int',
        'y': 'int'
    }

    attribute_map = {
        'force_range': 'forceRange',
        'h': 'h',
        'i': 'i',
        'id': 'id',
        'w': 'w',
        'widget': 'widget',
        'x': 'x',
        'y': 'y'
    }

    def __init__(self, force_range=None, h=None, i=None, id=None, w=None, widget=None, x=None, y=None):  # noqa: E501
        """WidgetCell - a model defined in Swagger"""  # noqa: E501

        self._force_range = None
        self._h = None
        self._i = None
        self._id = None
        self._w = None
        self._widget = None
        self._x = None
        self._y = None
        self.discriminator = None

        if force_range is not None:
            self.force_range = force_range
        if h is not None:
            self.h = h
        if i is not None:
            self.i = i
        if id is not None:
            self.id = id
        if w is not None:
            self.w = w
        if widget is not None:
            self.widget = widget
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @property
    def force_range(self):
        """Gets the force_range of this WidgetCell.  # noqa: E501


        :return: The force_range of this WidgetCell.  # noqa: E501
        :rtype: bool
        """
        return self._force_range

    @force_range.setter
    def force_range(self, force_range):
        """Sets the force_range of this WidgetCell.


        :param force_range: The force_range of this WidgetCell.  # noqa: E501
        :type: bool
        """

        self._force_range = force_range

    @property
    def h(self):
        """Gets the h of this WidgetCell.  # noqa: E501


        :return: The h of this WidgetCell.  # noqa: E501
        :rtype: int
        """
        return self._h

    @h.setter
    def h(self, h):
        """Sets the h of this WidgetCell.


        :param h: The h of this WidgetCell.  # noqa: E501
        :type: int
        """

        self._h = h

    @property
    def i(self):
        """Gets the i of this WidgetCell.  # noqa: E501


        :return: The i of this WidgetCell.  # noqa: E501
        :rtype: str
        """
        return self._i

    @i.setter
    def i(self, i):
        """Sets the i of this WidgetCell.


        :param i: The i of this WidgetCell.  # noqa: E501
        :type: str
        """

        self._i = i

    @property
    def id(self):
        """Gets the id of this WidgetCell.  # noqa: E501


        :return: The id of this WidgetCell.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WidgetCell.


        :param id: The id of this WidgetCell.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def w(self):
        """Gets the w of this WidgetCell.  # noqa: E501


        :return: The w of this WidgetCell.  # noqa: E501
        :rtype: int
        """
        return self._w

    @w.setter
    def w(self, w):
        """Sets the w of this WidgetCell.


        :param w: The w of this WidgetCell.  # noqa: E501
        :type: int
        """

        self._w = w

    @property
    def widget(self):
        """Gets the widget of this WidgetCell.  # noqa: E501


        :return: The widget of this WidgetCell.  # noqa: E501
        :rtype: Widget
        """
        return self._widget

    @widget.setter
    def widget(self, widget):
        """Sets the widget of this WidgetCell.


        :param widget: The widget of this WidgetCell.  # noqa: E501
        :type: Widget
        """

        self._widget = widget

    @property
    def x(self):
        """Gets the x of this WidgetCell.  # noqa: E501


        :return: The x of this WidgetCell.  # noqa: E501
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this WidgetCell.


        :param x: The x of this WidgetCell.  # noqa: E501
        :type: int
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this WidgetCell.  # noqa: E501


        :return: The y of this WidgetCell.  # noqa: E501
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this WidgetCell.


        :param y: The y of this WidgetCell.  # noqa: E501
        :type: int
        """

        self._y = y

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
        if issubclass(WidgetCell, dict):
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
        if not isinstance(other, WidgetCell):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
