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

from demisto_client.demisto_api.models.task_state import TaskState  # noqa: F401,E501


class InvPlaybookTaskCompleteData(object):
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
        'arguments': 'dict(str, object)',
        'completed_by': 'str',
        'completed_count': 'int',
        'completed_date': 'datetime',
        'entries': 'list[str]',
        'input': 'str',
        'outputs': 'dict(str, object)',
        'playbook_inputs': 'dict(str, object)',
        'start_date': 'datetime',
        'state': 'TaskState',
        'will_not_execute_count': 'int',
        'will_not_execute_reason': 'str'
    }

    attribute_map = {
        'arguments': 'arguments',
        'completed_by': 'completedBy',
        'completed_count': 'completedCount',
        'completed_date': 'completedDate',
        'entries': 'entries',
        'input': 'input',
        'outputs': 'outputs',
        'playbook_inputs': 'playbookInputs',
        'start_date': 'startDate',
        'state': 'state',
        'will_not_execute_count': 'willNotExecuteCount',
        'will_not_execute_reason': 'willNotExecuteReason'
    }

    def __init__(self, arguments=None, completed_by=None, completed_count=None, completed_date=None, entries=None, input=None, outputs=None, playbook_inputs=None, start_date=None, state=None, will_not_execute_count=None, will_not_execute_reason=None):  # noqa: E501
        """InvPlaybookTaskCompleteData - a model defined in Swagger"""  # noqa: E501

        self._arguments = None
        self._completed_by = None
        self._completed_count = None
        self._completed_date = None
        self._entries = None
        self._input = None
        self._outputs = None
        self._playbook_inputs = None
        self._start_date = None
        self._state = None
        self._will_not_execute_count = None
        self._will_not_execute_reason = None
        self.discriminator = None

        if arguments is not None:
            self.arguments = arguments
        if completed_by is not None:
            self.completed_by = completed_by
        if completed_count is not None:
            self.completed_count = completed_count
        if completed_date is not None:
            self.completed_date = completed_date
        if entries is not None:
            self.entries = entries
        if input is not None:
            self.input = input
        if outputs is not None:
            self.outputs = outputs
        if playbook_inputs is not None:
            self.playbook_inputs = playbook_inputs
        if start_date is not None:
            self.start_date = start_date
        if state is not None:
            self.state = state
        if will_not_execute_count is not None:
            self.will_not_execute_count = will_not_execute_count
        if will_not_execute_reason is not None:
            self.will_not_execute_reason = will_not_execute_reason

    @property
    def arguments(self):
        """Gets the arguments of this InvPlaybookTaskCompleteData.  # noqa: E501


        :return: The arguments of this InvPlaybookTaskCompleteData.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this InvPlaybookTaskCompleteData.


        :param arguments: The arguments of this InvPlaybookTaskCompleteData.  # noqa: E501
        :type: dict(str, object)
        """

        self._arguments = arguments

    @property
    def completed_by(self):
        """Gets the completed_by of this InvPlaybookTaskCompleteData.  # noqa: E501


        :return: The completed_by of this InvPlaybookTaskCompleteData.  # noqa: E501
        :rtype: str
        """
        return self._completed_by

    @completed_by.setter
    def completed_by(self, completed_by):
        """Sets the completed_by of this InvPlaybookTaskCompleteData.


        :param completed_by: The completed_by of this InvPlaybookTaskCompleteData.  # noqa: E501
        :type: str
        """

        self._completed_by = completed_by

    @property
    def completed_count(self):
        """Gets the completed_count of this InvPlaybookTaskCompleteData.  # noqa: E501


        :return: The completed_count of this InvPlaybookTaskCompleteData.  # noqa: E501
        :rtype: int
        """
        return self._completed_count

    @completed_count.setter
    def completed_count(self, completed_count):
        """Sets the completed_count of this InvPlaybookTaskCompleteData.


        :param completed_count: The completed_count of this InvPlaybookTaskCompleteData.  # noqa: E501
        :type: int
        """

        self._completed_count = completed_count

    @property
    def completed_date(self):
        """Gets the completed_date of this InvPlaybookTaskCompleteData.  # noqa: E501


        :return: The completed_date of this InvPlaybookTaskCompleteData.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_date

    @completed_date.setter
    def completed_date(self, completed_date):
        """Sets the completed_date of this InvPlaybookTaskCompleteData.


        :param completed_date: The completed_date of this InvPlaybookTaskCompleteData.  # noqa: E501
        :type: datetime
        """

        self._completed_date = completed_date

    @property
    def entries(self):
        """Gets the entries of this InvPlaybookTaskCompleteData.  # noqa: E501


        :return: The entries of this InvPlaybookTaskCompleteData.  # noqa: E501
        :rtype: list[str]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this InvPlaybookTaskCompleteData.


        :param entries: The entries of this InvPlaybookTaskCompleteData.  # noqa: E501
        :type: list[str]
        """

        self._entries = entries

    @property
    def input(self):
        """Gets the input of this InvPlaybookTaskCompleteData.  # noqa: E501


        :return: The input of this InvPlaybookTaskCompleteData.  # noqa: E501
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InvPlaybookTaskCompleteData.


        :param input: The input of this InvPlaybookTaskCompleteData.  # noqa: E501
        :type: str
        """

        self._input = input

    @property
    def outputs(self):
        """Gets the outputs of this InvPlaybookTaskCompleteData.  # noqa: E501


        :return: The outputs of this InvPlaybookTaskCompleteData.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this InvPlaybookTaskCompleteData.


        :param outputs: The outputs of this InvPlaybookTaskCompleteData.  # noqa: E501
        :type: dict(str, object)
        """

        self._outputs = outputs

    @property
    def playbook_inputs(self):
        """Gets the playbook_inputs of this InvPlaybookTaskCompleteData.  # noqa: E501


        :return: The playbook_inputs of this InvPlaybookTaskCompleteData.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._playbook_inputs

    @playbook_inputs.setter
    def playbook_inputs(self, playbook_inputs):
        """Sets the playbook_inputs of this InvPlaybookTaskCompleteData.


        :param playbook_inputs: The playbook_inputs of this InvPlaybookTaskCompleteData.  # noqa: E501
        :type: dict(str, object)
        """

        self._playbook_inputs = playbook_inputs

    @property
    def start_date(self):
        """Gets the start_date of this InvPlaybookTaskCompleteData.  # noqa: E501


        :return: The start_date of this InvPlaybookTaskCompleteData.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InvPlaybookTaskCompleteData.


        :param start_date: The start_date of this InvPlaybookTaskCompleteData.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def state(self):
        """Gets the state of this InvPlaybookTaskCompleteData.  # noqa: E501


        :return: The state of this InvPlaybookTaskCompleteData.  # noqa: E501
        :rtype: TaskState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InvPlaybookTaskCompleteData.


        :param state: The state of this InvPlaybookTaskCompleteData.  # noqa: E501
        :type: TaskState
        """

        self._state = state

    @property
    def will_not_execute_count(self):
        """Gets the will_not_execute_count of this InvPlaybookTaskCompleteData.  # noqa: E501


        :return: The will_not_execute_count of this InvPlaybookTaskCompleteData.  # noqa: E501
        :rtype: int
        """
        return self._will_not_execute_count

    @will_not_execute_count.setter
    def will_not_execute_count(self, will_not_execute_count):
        """Sets the will_not_execute_count of this InvPlaybookTaskCompleteData.


        :param will_not_execute_count: The will_not_execute_count of this InvPlaybookTaskCompleteData.  # noqa: E501
        :type: int
        """

        self._will_not_execute_count = will_not_execute_count

    @property
    def will_not_execute_reason(self):
        """Gets the will_not_execute_reason of this InvPlaybookTaskCompleteData.  # noqa: E501


        :return: The will_not_execute_reason of this InvPlaybookTaskCompleteData.  # noqa: E501
        :rtype: str
        """
        return self._will_not_execute_reason

    @will_not_execute_reason.setter
    def will_not_execute_reason(self, will_not_execute_reason):
        """Sets the will_not_execute_reason of this InvPlaybookTaskCompleteData.


        :param will_not_execute_reason: The will_not_execute_reason of this InvPlaybookTaskCompleteData.  # noqa: E501
        :type: str
        """

        self._will_not_execute_reason = will_not_execute_reason

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
        if issubclass(InvPlaybookTaskCompleteData, dict):
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
        if not isinstance(other, InvPlaybookTaskCompleteData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
