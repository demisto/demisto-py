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

from demisto.models.date_range import DateRange  # noqa: F401,E501
from demisto.models.order import Order  # noqa: F401,E501


class Widget(object):
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
        'category': 'str',
        'commit_message': 'str',
        'data_type': 'str',
        'date_range': 'DateRange',
        'description': 'str',
        'id': 'str',
        'is_predefined': 'bool',
        'locked': 'bool',
        'modified': 'datetime',
        'name': 'str',
        'params': 'dict(str, object)',
        'prev_name': 'str',
        'query': 'str',
        'should_commit': 'bool',
        'size': 'int',
        'sort': 'list[Order]',
        'sort_values': 'list[str]',
        'vc_should_ignore': 'bool',
        'version': 'int',
        'widget_type': 'str'
    }

    attribute_map = {
        'category': 'category',
        'commit_message': 'commitMessage',
        'data_type': 'dataType',
        'date_range': 'dateRange',
        'description': 'description',
        'id': 'id',
        'is_predefined': 'isPredefined',
        'locked': 'locked',
        'modified': 'modified',
        'name': 'name',
        'params': 'params',
        'prev_name': 'prevName',
        'query': 'query',
        'should_commit': 'shouldCommit',
        'size': 'size',
        'sort': 'sort',
        'sort_values': 'sortValues',
        'vc_should_ignore': 'vcShouldIgnore',
        'version': 'version',
        'widget_type': 'widgetType'
    }

    def __init__(self, category=None, commit_message=None, data_type=None, date_range=None, description=None, id=None, is_predefined=None, locked=None, modified=None, name=None, params=None, prev_name=None, query=None, should_commit=None, size=None, sort=None, sort_values=None, vc_should_ignore=None, version=None, widget_type=None):  # noqa: E501
        """Widget - a model defined in Swagger"""  # noqa: E501

        self._category = None
        self._commit_message = None
        self._data_type = None
        self._date_range = None
        self._description = None
        self._id = None
        self._is_predefined = None
        self._locked = None
        self._modified = None
        self._name = None
        self._params = None
        self._prev_name = None
        self._query = None
        self._should_commit = None
        self._size = None
        self._sort = None
        self._sort_values = None
        self._vc_should_ignore = None
        self._version = None
        self._widget_type = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if commit_message is not None:
            self.commit_message = commit_message
        if data_type is not None:
            self.data_type = data_type
        if date_range is not None:
            self.date_range = date_range
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_predefined is not None:
            self.is_predefined = is_predefined
        if locked is not None:
            self.locked = locked
        if modified is not None:
            self.modified = modified
        self.name = name
        if params is not None:
            self.params = params
        if prev_name is not None:
            self.prev_name = prev_name
        if query is not None:
            self.query = query
        if should_commit is not None:
            self.should_commit = should_commit
        if size is not None:
            self.size = size
        if sort is not None:
            self.sort = sort
        if sort_values is not None:
            self.sort_values = sort_values
        if vc_should_ignore is not None:
            self.vc_should_ignore = vc_should_ignore
        if version is not None:
            self.version = version
        self.widget_type = widget_type

    @property
    def category(self):
        """Gets the category of this Widget.  # noqa: E501

        Category the widget is related to. Used to display in widget library under category or dataType if empty.  # noqa: E501

        :return: The category of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Widget.

        Category the widget is related to. Used to display in widget library under category or dataType if empty.  # noqa: E501

        :param category: The category of this Widget.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def commit_message(self):
        """Gets the commit_message of this Widget.  # noqa: E501


        :return: The commit_message of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """Sets the commit_message of this Widget.


        :param commit_message: The commit_message of this Widget.  # noqa: E501
        :type: str
        """

        self._commit_message = commit_message

    @property
    def data_type(self):
        """Gets the data_type of this Widget.  # noqa: E501

        Data type of the widget. Describes what data does the widget query. supporting data types \"incidents\",\"messages\",\"system\",\"entries\",\"tasks\", \"audit\".  # noqa: E501

        :return: The data_type of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Widget.

        Data type of the widget. Describes what data does the widget query. supporting data types \"incidents\",\"messages\",\"system\",\"entries\",\"tasks\", \"audit\".  # noqa: E501

        :param data_type: The data_type of this Widget.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def date_range(self):
        """Gets the date_range of this Widget.  # noqa: E501


        :return: The date_range of this Widget.  # noqa: E501
        :rtype: DateRange
        """
        return self._date_range

    @date_range.setter
    def date_range(self, date_range):
        """Sets the date_range of this Widget.


        :param date_range: The date_range of this Widget.  # noqa: E501
        :type: DateRange
        """

        self._date_range = date_range

    @property
    def description(self):
        """Gets the description of this Widget.  # noqa: E501

        The description of the widget's usage and data representation.  # noqa: E501

        :return: The description of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Widget.

        The description of the widget's usage and data representation.  # noqa: E501

        :param description: The description of this Widget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Widget.  # noqa: E501


        :return: The id of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Widget.


        :param id: The id of this Widget.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_predefined(self):
        """Gets the is_predefined of this Widget.  # noqa: E501

        Is the widget a system widget.  # noqa: E501

        :return: The is_predefined of this Widget.  # noqa: E501
        :rtype: bool
        """
        return self._is_predefined

    @is_predefined.setter
    def is_predefined(self, is_predefined):
        """Sets the is_predefined of this Widget.

        Is the widget a system widget.  # noqa: E501

        :param is_predefined: The is_predefined of this Widget.  # noqa: E501
        :type: bool
        """

        self._is_predefined = is_predefined

    @property
    def locked(self):
        """Gets the locked of this Widget.  # noqa: E501

        Is the widget locked for editing.  # noqa: E501

        :return: The locked of this Widget.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this Widget.

        Is the widget locked for editing.  # noqa: E501

        :param locked: The locked of this Widget.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def modified(self):
        """Gets the modified of this Widget.  # noqa: E501


        :return: The modified of this Widget.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Widget.


        :param modified: The modified of this Widget.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this Widget.  # noqa: E501

        Default name of the widget.  # noqa: E501

        :return: The name of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Widget.

        Default name of the widget.  # noqa: E501

        :param name: The name of this Widget.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def params(self):
        """Gets the params of this Widget.  # noqa: E501

        Additional parameters for this widget, depends on widget type and data.  # noqa: E501

        :return: The params of this Widget.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this Widget.

        Additional parameters for this widget, depends on widget type and data.  # noqa: E501

        :param params: The params of this Widget.  # noqa: E501
        :type: dict(str, object)
        """

        self._params = params

    @property
    def prev_name(self):
        """Gets the prev_name of this Widget.  # noqa: E501

        The previous name of the widget.  # noqa: E501

        :return: The prev_name of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._prev_name

    @prev_name.setter
    def prev_name(self, prev_name):
        """Sets the prev_name of this Widget.

        The previous name of the widget.  # noqa: E501

        :param prev_name: The prev_name of this Widget.  # noqa: E501
        :type: str
        """

        self._prev_name = prev_name

    @property
    def query(self):
        """Gets the query of this Widget.  # noqa: E501

        Query to search on the dataType.  # noqa: E501

        :return: The query of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this Widget.

        Query to search on the dataType.  # noqa: E501

        :param query: The query of this Widget.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def should_commit(self):
        """Gets the should_commit of this Widget.  # noqa: E501


        :return: The should_commit of this Widget.  # noqa: E501
        :rtype: bool
        """
        return self._should_commit

    @should_commit.setter
    def should_commit(self, should_commit):
        """Sets the should_commit of this Widget.


        :param should_commit: The should_commit of this Widget.  # noqa: E501
        :type: bool
        """

        self._should_commit = should_commit

    @property
    def size(self):
        """Gets the size of this Widget.  # noqa: E501

        Maximum size for this widget data returned.  # noqa: E501

        :return: The size of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Widget.

        Maximum size for this widget data returned.  # noqa: E501

        :param size: The size of this Widget.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def sort(self):
        """Gets the sort of this Widget.  # noqa: E501

        Sorting array to sort the data received by the given Order parameters.  # noqa: E501

        :return: The sort of this Widget.  # noqa: E501
        :rtype: list[Order]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this Widget.

        Sorting array to sort the data received by the given Order parameters.  # noqa: E501

        :param sort: The sort of this Widget.  # noqa: E501
        :type: list[Order]
        """

        self._sort = sort

    @property
    def sort_values(self):
        """Gets the sort_values of this Widget.  # noqa: E501


        :return: The sort_values of this Widget.  # noqa: E501
        :rtype: list[str]
        """
        return self._sort_values

    @sort_values.setter
    def sort_values(self, sort_values):
        """Sets the sort_values of this Widget.


        :param sort_values: The sort_values of this Widget.  # noqa: E501
        :type: list[str]
        """

        self._sort_values = sort_values

    @property
    def vc_should_ignore(self):
        """Gets the vc_should_ignore of this Widget.  # noqa: E501


        :return: The vc_should_ignore of this Widget.  # noqa: E501
        :rtype: bool
        """
        return self._vc_should_ignore

    @vc_should_ignore.setter
    def vc_should_ignore(self, vc_should_ignore):
        """Sets the vc_should_ignore of this Widget.


        :param vc_should_ignore: The vc_should_ignore of this Widget.  # noqa: E501
        :type: bool
        """

        self._vc_should_ignore = vc_should_ignore

    @property
    def version(self):
        """Gets the version of this Widget.  # noqa: E501


        :return: The version of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Widget.


        :param version: The version of this Widget.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def widget_type(self):
        """Gets the widget_type of this Widget.  # noqa: E501

        Widget type describes how does the widget should recieve the data, and display it. Supporting types: \"bar\", \"column\", \"pie\", \"list\", \"number\", \"trend\", \"text\", \"duration\", \"image\", \"line\", and \"table\".  # noqa: E501

        :return: The widget_type of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._widget_type

    @widget_type.setter
    def widget_type(self, widget_type):
        """Sets the widget_type of this Widget.

        Widget type describes how does the widget should recieve the data, and display it. Supporting types: \"bar\", \"column\", \"pie\", \"list\", \"number\", \"trend\", \"text\", \"duration\", \"image\", \"line\", and \"table\".  # noqa: E501

        :param widget_type: The widget_type of this Widget.  # noqa: E501
        :type: str
        """
        if widget_type is None:
            raise ValueError("Invalid value for `widget_type`, must not be `None`")  # noqa: E501

        self._widget_type = widget_type

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
        if issubclass(Widget, dict):
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
        if not isinstance(other, Widget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
