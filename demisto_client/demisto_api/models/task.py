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

from demisto_client.demisto_api.models.task_type import TaskType  # noqa: F401,E501


class Task(object):
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
        'brand': 'str',
        'cloned_from': 'str',
        'comment': 'str',
        'conditions': 'list[str]',
        'description': 'str',
        'id': 'str',
        'is_command': 'bool',
        'is_locked': 'bool',
        'is_system_task': 'bool',
        'is_title_task': 'bool',
        'modified': 'datetime',
        'name': 'str',
        'playbook_id': 'str',
        'script_id': 'str',
        'sort_values': 'list[str]',
        'tags': 'list[str]',
        'type': 'TaskType',
        'version': 'int'
    }

    attribute_map = {
        'brand': 'brand',
        'cloned_from': 'clonedFrom',
        'comment': 'comment',
        'conditions': 'conditions',
        'description': 'description',
        'id': 'id',
        'is_command': 'isCommand',
        'is_locked': 'isLocked',
        'is_system_task': 'isSystemTask',
        'is_title_task': 'isTitleTask',
        'modified': 'modified',
        'name': 'name',
        'playbook_id': 'playbookId',
        'script_id': 'scriptId',
        'sort_values': 'sortValues',
        'tags': 'tags',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, brand=None, cloned_from=None, comment=None, conditions=None, description=None, id=None, is_command=None, is_locked=None, is_system_task=None, is_title_task=None, modified=None, name=None, playbook_id=None, script_id=None, sort_values=None, tags=None, type=None, version=None):  # noqa: E501
        """Task - a model defined in Swagger"""  # noqa: E501

        self._brand = None
        self._cloned_from = None
        self._comment = None
        self._conditions = None
        self._description = None
        self._id = None
        self._is_command = None
        self._is_locked = None
        self._is_system_task = None
        self._is_title_task = None
        self._modified = None
        self._name = None
        self._playbook_id = None
        self._script_id = None
        self._sort_values = None
        self._tags = None
        self._type = None
        self._version = None
        self.discriminator = None

        if brand is not None:
            self.brand = brand
        if cloned_from is not None:
            self.cloned_from = cloned_from
        if comment is not None:
            self.comment = comment
        if conditions is not None:
            self.conditions = conditions
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_command is not None:
            self.is_command = is_command
        if is_locked is not None:
            self.is_locked = is_locked
        if is_system_task is not None:
            self.is_system_task = is_system_task
        if is_title_task is not None:
            self.is_title_task = is_title_task
        if modified is not None:
            self.modified = modified
        if name is not None:
            self.name = name
        if playbook_id is not None:
            self.playbook_id = playbook_id
        if script_id is not None:
            self.script_id = script_id
        if sort_values is not None:
            self.sort_values = sort_values
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def brand(self):
        """Gets the brand of this Task.  # noqa: E501


        :return: The brand of this Task.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this Task.


        :param brand: The brand of this Task.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def cloned_from(self):
        """Gets the cloned_from of this Task.  # noqa: E501


        :return: The cloned_from of this Task.  # noqa: E501
        :rtype: str
        """
        return self._cloned_from

    @cloned_from.setter
    def cloned_from(self, cloned_from):
        """Sets the cloned_from of this Task.


        :param cloned_from: The cloned_from of this Task.  # noqa: E501
        :type: str
        """

        self._cloned_from = cloned_from

    @property
    def comment(self):
        """Gets the comment of this Task.  # noqa: E501


        :return: The comment of this Task.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Task.


        :param comment: The comment of this Task.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def conditions(self):
        """Gets the conditions of this Task.  # noqa: E501


        :return: The conditions of this Task.  # noqa: E501
        :rtype: list[str]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this Task.


        :param conditions: The conditions of this Task.  # noqa: E501
        :type: list[str]
        """

        self._conditions = conditions

    @property
    def description(self):
        """Gets the description of this Task.  # noqa: E501


        :return: The description of this Task.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Task.


        :param description: The description of this Task.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Task.  # noqa: E501


        :return: The id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Task.


        :param id: The id of this Task.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_command(self):
        """Gets the is_command of this Task.  # noqa: E501


        :return: The is_command of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_command

    @is_command.setter
    def is_command(self, is_command):
        """Sets the is_command of this Task.


        :param is_command: The is_command of this Task.  # noqa: E501
        :type: bool
        """

        self._is_command = is_command

    @property
    def is_locked(self):
        """Gets the is_locked of this Task.  # noqa: E501


        :return: The is_locked of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this Task.


        :param is_locked: The is_locked of this Task.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def is_system_task(self):
        """Gets the is_system_task of this Task.  # noqa: E501


        :return: The is_system_task of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_system_task

    @is_system_task.setter
    def is_system_task(self, is_system_task):
        """Sets the is_system_task of this Task.


        :param is_system_task: The is_system_task of this Task.  # noqa: E501
        :type: bool
        """

        self._is_system_task = is_system_task

    @property
    def is_title_task(self):
        """Gets the is_title_task of this Task.  # noqa: E501


        :return: The is_title_task of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_title_task

    @is_title_task.setter
    def is_title_task(self, is_title_task):
        """Sets the is_title_task of this Task.


        :param is_title_task: The is_title_task of this Task.  # noqa: E501
        :type: bool
        """

        self._is_title_task = is_title_task

    @property
    def modified(self):
        """Gets the modified of this Task.  # noqa: E501


        :return: The modified of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Task.


        :param modified: The modified of this Task.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this Task.  # noqa: E501


        :return: The name of this Task.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Task.


        :param name: The name of this Task.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def playbook_id(self):
        """Gets the playbook_id of this Task.  # noqa: E501


        :return: The playbook_id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        """Sets the playbook_id of this Task.


        :param playbook_id: The playbook_id of this Task.  # noqa: E501
        :type: str
        """

        self._playbook_id = playbook_id

    @property
    def script_id(self):
        """Gets the script_id of this Task.  # noqa: E501


        :return: The script_id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this Task.


        :param script_id: The script_id of this Task.  # noqa: E501
        :type: str
        """

        self._script_id = script_id

    @property
    def sort_values(self):
        """Gets the sort_values of this Task.  # noqa: E501


        :return: The sort_values of this Task.  # noqa: E501
        :rtype: list[str]
        """
        return self._sort_values

    @sort_values.setter
    def sort_values(self, sort_values):
        """Sets the sort_values of this Task.


        :param sort_values: The sort_values of this Task.  # noqa: E501
        :type: list[str]
        """

        self._sort_values = sort_values

    @property
    def tags(self):
        """Gets the tags of this Task.  # noqa: E501


        :return: The tags of this Task.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Task.


        :param tags: The tags of this Task.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this Task.  # noqa: E501


        :return: The type of this Task.  # noqa: E501
        :rtype: TaskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Task.


        :param type: The type of this Task.  # noqa: E501
        :type: TaskType
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this Task.  # noqa: E501


        :return: The version of this Task.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Task.


        :param version: The version of this Task.  # noqa: E501
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
        if issubclass(Task, dict):
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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
