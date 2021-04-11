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

from demisto_client.demisto_api.models.advance_arg import AdvanceArg  # noqa: F401,E501
from demisto_client.demisto_api.models.task_loop import TaskLoop  # noqa: F401,E501
from demisto_client.demisto_api.models.task_type import TaskType  # noqa: F401,E501


class InvPlaybookTaskData(object):
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
        'add_after': 'bool',
        'automation_script': 'str',
        'description': 'str',
        'loop': 'TaskLoop',
        'name': 'str',
        'neighbor_inv_pb_task_id': 'str',
        'playbook_id': 'str',
        'script_arguments': 'dict(str, AdvanceArg)',
        'separate_context': 'bool',
        'tags': 'list[str]',
        'type': 'TaskType'
    }

    attribute_map = {
        'add_after': 'addAfter',
        'automation_script': 'automationScript',
        'description': 'description',
        'loop': 'loop',
        'name': 'name',
        'neighbor_inv_pb_task_id': 'neighborInvPBTaskId',
        'playbook_id': 'playbookId',
        'script_arguments': 'scriptArguments',
        'separate_context': 'separateContext',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, add_after=None, automation_script=None, description=None, loop=None, name=None, neighbor_inv_pb_task_id=None, playbook_id=None, script_arguments=None, separate_context=None, tags=None, type=None):  # noqa: E501
        """InvPlaybookTaskData - a model defined in Swagger"""  # noqa: E501

        self._add_after = None
        self._automation_script = None
        self._description = None
        self._loop = None
        self._name = None
        self._neighbor_inv_pb_task_id = None
        self._playbook_id = None
        self._script_arguments = None
        self._separate_context = None
        self._tags = None
        self._type = None
        self.discriminator = None

        if add_after is not None:
            self.add_after = add_after
        if automation_script is not None:
            self.automation_script = automation_script
        if description is not None:
            self.description = description
        if loop is not None:
            self.loop = loop
        if name is not None:
            self.name = name
        if neighbor_inv_pb_task_id is not None:
            self.neighbor_inv_pb_task_id = neighbor_inv_pb_task_id
        if playbook_id is not None:
            self.playbook_id = playbook_id
        if script_arguments is not None:
            self.script_arguments = script_arguments
        if separate_context is not None:
            self.separate_context = separate_context
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type

    @property
    def add_after(self):
        """Gets the add_after of this InvPlaybookTaskData.  # noqa: E501


        :return: The add_after of this InvPlaybookTaskData.  # noqa: E501
        :rtype: bool
        """
        return self._add_after

    @add_after.setter
    def add_after(self, add_after):
        """Sets the add_after of this InvPlaybookTaskData.


        :param add_after: The add_after of this InvPlaybookTaskData.  # noqa: E501
        :type: bool
        """

        self._add_after = add_after

    @property
    def automation_script(self):
        """Gets the automation_script of this InvPlaybookTaskData.  # noqa: E501


        :return: The automation_script of this InvPlaybookTaskData.  # noqa: E501
        :rtype: str
        """
        return self._automation_script

    @automation_script.setter
    def automation_script(self, automation_script):
        """Sets the automation_script of this InvPlaybookTaskData.


        :param automation_script: The automation_script of this InvPlaybookTaskData.  # noqa: E501
        :type: str
        """

        self._automation_script = automation_script

    @property
    def description(self):
        """Gets the description of this InvPlaybookTaskData.  # noqa: E501


        :return: The description of this InvPlaybookTaskData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InvPlaybookTaskData.


        :param description: The description of this InvPlaybookTaskData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def loop(self):
        """Gets the loop of this InvPlaybookTaskData.  # noqa: E501


        :return: The loop of this InvPlaybookTaskData.  # noqa: E501
        :rtype: TaskLoop
        """
        return self._loop

    @loop.setter
    def loop(self, loop):
        """Sets the loop of this InvPlaybookTaskData.


        :param loop: The loop of this InvPlaybookTaskData.  # noqa: E501
        :type: TaskLoop
        """

        self._loop = loop

    @property
    def name(self):
        """Gets the name of this InvPlaybookTaskData.  # noqa: E501


        :return: The name of this InvPlaybookTaskData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InvPlaybookTaskData.


        :param name: The name of this InvPlaybookTaskData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def neighbor_inv_pb_task_id(self):
        """Gets the neighbor_inv_pb_task_id of this InvPlaybookTaskData.  # noqa: E501


        :return: The neighbor_inv_pb_task_id of this InvPlaybookTaskData.  # noqa: E501
        :rtype: str
        """
        return self._neighbor_inv_pb_task_id

    @neighbor_inv_pb_task_id.setter
    def neighbor_inv_pb_task_id(self, neighbor_inv_pb_task_id):
        """Sets the neighbor_inv_pb_task_id of this InvPlaybookTaskData.


        :param neighbor_inv_pb_task_id: The neighbor_inv_pb_task_id of this InvPlaybookTaskData.  # noqa: E501
        :type: str
        """

        self._neighbor_inv_pb_task_id = neighbor_inv_pb_task_id

    @property
    def playbook_id(self):
        """Gets the playbook_id of this InvPlaybookTaskData.  # noqa: E501


        :return: The playbook_id of this InvPlaybookTaskData.  # noqa: E501
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        """Sets the playbook_id of this InvPlaybookTaskData.


        :param playbook_id: The playbook_id of this InvPlaybookTaskData.  # noqa: E501
        :type: str
        """

        self._playbook_id = playbook_id

    @property
    def script_arguments(self):
        """Gets the script_arguments of this InvPlaybookTaskData.  # noqa: E501


        :return: The script_arguments of this InvPlaybookTaskData.  # noqa: E501
        :rtype: dict(str, AdvanceArg)
        """
        return self._script_arguments

    @script_arguments.setter
    def script_arguments(self, script_arguments):
        """Sets the script_arguments of this InvPlaybookTaskData.


        :param script_arguments: The script_arguments of this InvPlaybookTaskData.  # noqa: E501
        :type: dict(str, AdvanceArg)
        """

        self._script_arguments = script_arguments

    @property
    def separate_context(self):
        """Gets the separate_context of this InvPlaybookTaskData.  # noqa: E501


        :return: The separate_context of this InvPlaybookTaskData.  # noqa: E501
        :rtype: bool
        """
        return self._separate_context

    @separate_context.setter
    def separate_context(self, separate_context):
        """Sets the separate_context of this InvPlaybookTaskData.


        :param separate_context: The separate_context of this InvPlaybookTaskData.  # noqa: E501
        :type: bool
        """

        self._separate_context = separate_context

    @property
    def tags(self):
        """Gets the tags of this InvPlaybookTaskData.  # noqa: E501


        :return: The tags of this InvPlaybookTaskData.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InvPlaybookTaskData.


        :param tags: The tags of this InvPlaybookTaskData.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this InvPlaybookTaskData.  # noqa: E501


        :return: The type of this InvPlaybookTaskData.  # noqa: E501
        :rtype: TaskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InvPlaybookTaskData.


        :param type: The type of this InvPlaybookTaskData.  # noqa: E501
        :type: TaskType
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
        if issubclass(InvPlaybookTaskData, dict):
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
        if not isinstance(other, InvPlaybookTaskData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
