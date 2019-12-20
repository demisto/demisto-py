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


class Evidence(object):
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
        'shard_id': 'int',
        'description': 'str',
        'entry_id': 'str',
        'fetched': 'datetime',
        'has_role': 'bool',
        'id': 'str',
        'incident_id': 'str',
        'marked_by': 'str',
        'marked_date': 'datetime',
        'modified': 'datetime',
        'occurred': 'datetime',
        'previous_roles': 'list[str]',
        'roles': 'list[str]',
        'sort_values': 'list[str]',
        'tags': 'list[str]',
        'tags_raw': 'list[str]',
        'task_id': 'str',
        'version': 'int'
    }

    attribute_map = {
        'shard_id': 'ShardID',
        'description': 'description',
        'entry_id': 'entryId',
        'fetched': 'fetched',
        'has_role': 'hasRole',
        'id': 'id',
        'incident_id': 'incidentId',
        'marked_by': 'markedBy',
        'marked_date': 'markedDate',
        'modified': 'modified',
        'occurred': 'occurred',
        'previous_roles': 'previousRoles',
        'roles': 'roles',
        'sort_values': 'sortValues',
        'tags': 'tags',
        'tags_raw': 'tagsRaw',
        'task_id': 'taskId',
        'version': 'version'
    }

    def __init__(self, shard_id=None, description=None, entry_id=None, fetched=None, has_role=None, id=None, incident_id=None, marked_by=None, marked_date=None, modified=None, occurred=None, previous_roles=None, roles=None, sort_values=None, tags=None, tags_raw=None, task_id=None, version=None):  # noqa: E501
        """Evidence - a model defined in Swagger"""  # noqa: E501

        self._shard_id = None
        self._description = None
        self._entry_id = None
        self._fetched = None
        self._has_role = None
        self._id = None
        self._incident_id = None
        self._marked_by = None
        self._marked_date = None
        self._modified = None
        self._occurred = None
        self._previous_roles = None
        self._roles = None
        self._sort_values = None
        self._tags = None
        self._tags_raw = None
        self._task_id = None
        self._version = None
        self.discriminator = None

        if shard_id is not None:
            self.shard_id = shard_id
        if description is not None:
            self.description = description
        if entry_id is not None:
            self.entry_id = entry_id
        if fetched is not None:
            self.fetched = fetched
        if has_role is not None:
            self.has_role = has_role
        if id is not None:
            self.id = id
        if incident_id is not None:
            self.incident_id = incident_id
        if marked_by is not None:
            self.marked_by = marked_by
        if marked_date is not None:
            self.marked_date = marked_date
        if modified is not None:
            self.modified = modified
        if occurred is not None:
            self.occurred = occurred
        if previous_roles is not None:
            self.previous_roles = previous_roles
        if roles is not None:
            self.roles = roles
        if sort_values is not None:
            self.sort_values = sort_values
        if tags is not None:
            self.tags = tags
        if tags_raw is not None:
            self.tags_raw = tags_raw
        if task_id is not None:
            self.task_id = task_id
        if version is not None:
            self.version = version

    @property
    def shard_id(self):
        """Gets the shard_id of this Evidence.  # noqa: E501


        :return: The shard_id of this Evidence.  # noqa: E501
        :rtype: int
        """
        return self._shard_id

    @shard_id.setter
    def shard_id(self, shard_id):
        """Sets the shard_id of this Evidence.


        :param shard_id: The shard_id of this Evidence.  # noqa: E501
        :type: int
        """

        self._shard_id = shard_id

    @property
    def description(self):
        """Gets the description of this Evidence.  # noqa: E501

        The description for the resolve  # noqa: E501

        :return: The description of this Evidence.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Evidence.

        The description for the resolve  # noqa: E501

        :param description: The description of this Evidence.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def entry_id(self):
        """Gets the entry_id of this Evidence.  # noqa: E501

        The entry ID  # noqa: E501

        :return: The entry_id of this Evidence.  # noqa: E501
        :rtype: str
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this Evidence.

        The entry ID  # noqa: E501

        :param entry_id: The entry_id of this Evidence.  # noqa: E501
        :type: str
        """

        self._entry_id = entry_id

    @property
    def fetched(self):
        """Gets the fetched of this Evidence.  # noqa: E501

        when the evidence entry was fetched  # noqa: E501

        :return: The fetched of this Evidence.  # noqa: E501
        :rtype: datetime
        """
        return self._fetched

    @fetched.setter
    def fetched(self, fetched):
        """Sets the fetched of this Evidence.

        when the evidence entry was fetched  # noqa: E501

        :param fetched: The fetched of this Evidence.  # noqa: E501
        :type: datetime
        """

        self._fetched = fetched

    @property
    def has_role(self):
        """Gets the has_role of this Evidence.  # noqa: E501

        Internal field to make queries on role faster  # noqa: E501

        :return: The has_role of this Evidence.  # noqa: E501
        :rtype: bool
        """
        return self._has_role

    @has_role.setter
    def has_role(self, has_role):
        """Sets the has_role of this Evidence.

        Internal field to make queries on role faster  # noqa: E501

        :param has_role: The has_role of this Evidence.  # noqa: E501
        :type: bool
        """

        self._has_role = has_role

    @property
    def id(self):
        """Gets the id of this Evidence.  # noqa: E501


        :return: The id of this Evidence.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Evidence.


        :param id: The id of this Evidence.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def incident_id(self):
        """Gets the incident_id of this Evidence.  # noqa: E501

        The incident ID  # noqa: E501

        :return: The incident_id of this Evidence.  # noqa: E501
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this Evidence.

        The incident ID  # noqa: E501

        :param incident_id: The incident_id of this Evidence.  # noqa: E501
        :type: str
        """

        self._incident_id = incident_id

    @property
    def marked_by(self):
        """Gets the marked_by of this Evidence.  # noqa: E501

        the user that marked this evidence  # noqa: E501

        :return: The marked_by of this Evidence.  # noqa: E501
        :rtype: str
        """
        return self._marked_by

    @marked_by.setter
    def marked_by(self, marked_by):
        """Sets the marked_by of this Evidence.

        the user that marked this evidence  # noqa: E501

        :param marked_by: The marked_by of this Evidence.  # noqa: E501
        :type: str
        """

        self._marked_by = marked_by

    @property
    def marked_date(self):
        """Gets the marked_date of this Evidence.  # noqa: E501

        when this evidence was marked  # noqa: E501

        :return: The marked_date of this Evidence.  # noqa: E501
        :rtype: datetime
        """
        return self._marked_date

    @marked_date.setter
    def marked_date(self, marked_date):
        """Sets the marked_date of this Evidence.

        when this evidence was marked  # noqa: E501

        :param marked_date: The marked_date of this Evidence.  # noqa: E501
        :type: datetime
        """

        self._marked_date = marked_date

    @property
    def modified(self):
        """Gets the modified of this Evidence.  # noqa: E501


        :return: The modified of this Evidence.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Evidence.


        :param modified: The modified of this Evidence.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def occurred(self):
        """Gets the occurred of this Evidence.  # noqa: E501

        When this evidence has occurred  # noqa: E501

        :return: The occurred of this Evidence.  # noqa: E501
        :rtype: datetime
        """
        return self._occurred

    @occurred.setter
    def occurred(self, occurred):
        """Sets the occurred of this Evidence.

        When this evidence has occurred  # noqa: E501

        :param occurred: The occurred of this Evidence.  # noqa: E501
        :type: datetime
        """

        self._occurred = occurred

    @property
    def previous_roles(self):
        """Gets the previous_roles of this Evidence.  # noqa: E501

        PreviousRoleName - do not change this field manually  # noqa: E501

        :return: The previous_roles of this Evidence.  # noqa: E501
        :rtype: list[str]
        """
        return self._previous_roles

    @previous_roles.setter
    def previous_roles(self, previous_roles):
        """Sets the previous_roles of this Evidence.

        PreviousRoleName - do not change this field manually  # noqa: E501

        :param previous_roles: The previous_roles of this Evidence.  # noqa: E501
        :type: list[str]
        """

        self._previous_roles = previous_roles

    @property
    def roles(self):
        """Gets the roles of this Evidence.  # noqa: E501

        The role assigned to this investigation  # noqa: E501

        :return: The roles of this Evidence.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this Evidence.

        The role assigned to this investigation  # noqa: E501

        :param roles: The roles of this Evidence.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def sort_values(self):
        """Gets the sort_values of this Evidence.  # noqa: E501


        :return: The sort_values of this Evidence.  # noqa: E501
        :rtype: list[str]
        """
        return self._sort_values

    @sort_values.setter
    def sort_values(self, sort_values):
        """Sets the sort_values of this Evidence.


        :param sort_values: The sort_values of this Evidence.  # noqa: E501
        :type: list[str]
        """

        self._sort_values = sort_values

    @property
    def tags(self):
        """Gets the tags of this Evidence.  # noqa: E501

        Tags  # noqa: E501

        :return: The tags of this Evidence.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Evidence.

        Tags  # noqa: E501

        :param tags: The tags of this Evidence.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def tags_raw(self):
        """Gets the tags_raw of this Evidence.  # noqa: E501

        TagsRaw  # noqa: E501

        :return: The tags_raw of this Evidence.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags_raw

    @tags_raw.setter
    def tags_raw(self, tags_raw):
        """Sets the tags_raw of this Evidence.

        TagsRaw  # noqa: E501

        :param tags_raw: The tags_raw of this Evidence.  # noqa: E501
        :type: list[str]
        """

        self._tags_raw = tags_raw

    @property
    def task_id(self):
        """Gets the task_id of this Evidence.  # noqa: E501

        when the evidence entry was fetched  # noqa: E501

        :return: The task_id of this Evidence.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this Evidence.

        when the evidence entry was fetched  # noqa: E501

        :param task_id: The task_id of this Evidence.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def version(self):
        """Gets the version of this Evidence.  # noqa: E501


        :return: The version of this Evidence.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Evidence.


        :param version: The version of this Evidence.  # noqa: E501
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
        if issubclass(Evidence, dict):
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
        if not isinstance(other, Evidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
