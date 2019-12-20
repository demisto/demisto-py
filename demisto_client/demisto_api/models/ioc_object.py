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

from demisto_client.demisto_api.models.comments import Comments  # noqa: F401,E501
from demisto_client.demisto_api.models.custom_fields import CustomFields  # noqa: F401,E501
from demisto_client.demisto_api.models.feed_indicator import FeedIndicator  # noqa: F401,E501
from demisto_client.demisto_api.models.insight_cache import InsightCache  # noqa: F401,E501


class IocObject(object):
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
        'custom_fields': 'CustomFields',
        'account': 'str',
        'calculated_time': 'datetime',
        'comment': 'str',
        'comments': 'Comments',
        'first_seen': 'datetime',
        'first_seen_entry_id': 'str',
        'id': 'str',
        'indicator_type': 'str',
        'insight_cache': 'InsightCache',
        'investigation_i_ds': 'list[str]',
        'last_reputation_run': 'datetime',
        'last_seen': 'datetime',
        'last_seen_entry_id': 'str',
        'manual_score': 'bool',
        'manual_set_time': 'datetime',
        'manually_edited_fields': 'list[str]',
        'modified': 'datetime',
        'modified_time': 'datetime',
        'module_to_feed_map': 'dict(str, FeedIndicator)',
        'score': 'int',
        'set_by': 'str',
        'sort_values': 'list[str]',
        'source': 'str',
        'source_brands': 'list[str]',
        'source_instances': 'list[str]',
        'timestamp': 'datetime',
        'value': 'str',
        'version': 'int'
    }

    attribute_map = {
        'custom_fields': 'CustomFields',
        'account': 'account',
        'calculated_time': 'calculatedTime',
        'comment': 'comment',
        'comments': 'comments',
        'first_seen': 'firstSeen',
        'first_seen_entry_id': 'firstSeenEntryID',
        'id': 'id',
        'indicator_type': 'indicator_type',
        'insight_cache': 'insightCache',
        'investigation_i_ds': 'investigationIDs',
        'last_reputation_run': 'lastReputationRun',
        'last_seen': 'lastSeen',
        'last_seen_entry_id': 'lastSeenEntryID',
        'manual_score': 'manualScore',
        'manual_set_time': 'manualSetTime',
        'manually_edited_fields': 'manuallyEditedFields',
        'modified': 'modified',
        'modified_time': 'modifiedTime',
        'module_to_feed_map': 'moduleToFeedMap',
        'score': 'score',
        'set_by': 'setBy',
        'sort_values': 'sortValues',
        'source': 'source',
        'source_brands': 'sourceBrands',
        'source_instances': 'sourceInstances',
        'timestamp': 'timestamp',
        'value': 'value',
        'version': 'version'
    }

    def __init__(self, custom_fields=None, account=None, calculated_time=None, comment=None, comments=None, first_seen=None, first_seen_entry_id=None, id=None, indicator_type=None, insight_cache=None, investigation_i_ds=None, last_reputation_run=None, last_seen=None, last_seen_entry_id=None, manual_score=None, manual_set_time=None, manually_edited_fields=None, modified=None, modified_time=None, module_to_feed_map=None, score=None, set_by=None, sort_values=None, source=None, source_brands=None, source_instances=None, timestamp=None, value=None, version=None):  # noqa: E501
        """IocObject - a model defined in Swagger"""  # noqa: E501

        self._custom_fields = None
        self._account = None
        self._calculated_time = None
        self._comment = None
        self._comments = None
        self._first_seen = None
        self._first_seen_entry_id = None
        self._id = None
        self._indicator_type = None
        self._insight_cache = None
        self._investigation_i_ds = None
        self._last_reputation_run = None
        self._last_seen = None
        self._last_seen_entry_id = None
        self._manual_score = None
        self._manual_set_time = None
        self._manually_edited_fields = None
        self._modified = None
        self._modified_time = None
        self._module_to_feed_map = None
        self._score = None
        self._set_by = None
        self._sort_values = None
        self._source = None
        self._source_brands = None
        self._source_instances = None
        self._timestamp = None
        self._value = None
        self._version = None
        self.discriminator = None

        if custom_fields is not None:
            self.custom_fields = custom_fields
        if account is not None:
            self.account = account
        if calculated_time is not None:
            self.calculated_time = calculated_time
        if comment is not None:
            self.comment = comment
        if comments is not None:
            self.comments = comments
        if first_seen is not None:
            self.first_seen = first_seen
        if first_seen_entry_id is not None:
            self.first_seen_entry_id = first_seen_entry_id
        if id is not None:
            self.id = id
        if indicator_type is not None:
            self.indicator_type = indicator_type
        if insight_cache is not None:
            self.insight_cache = insight_cache
        if investigation_i_ds is not None:
            self.investigation_i_ds = investigation_i_ds
        if last_reputation_run is not None:
            self.last_reputation_run = last_reputation_run
        if last_seen is not None:
            self.last_seen = last_seen
        if last_seen_entry_id is not None:
            self.last_seen_entry_id = last_seen_entry_id
        if manual_score is not None:
            self.manual_score = manual_score
        if manual_set_time is not None:
            self.manual_set_time = manual_set_time
        if manually_edited_fields is not None:
            self.manually_edited_fields = manually_edited_fields
        if modified is not None:
            self.modified = modified
        if modified_time is not None:
            self.modified_time = modified_time
        if module_to_feed_map is not None:
            self.module_to_feed_map = module_to_feed_map
        if score is not None:
            self.score = score
        if set_by is not None:
            self.set_by = set_by
        if sort_values is not None:
            self.sort_values = sort_values
        if source is not None:
            self.source = source
        if source_brands is not None:
            self.source_brands = source_brands
        if source_instances is not None:
            self.source_instances = source_instances
        if timestamp is not None:
            self.timestamp = timestamp
        if value is not None:
            self.value = value
        if version is not None:
            self.version = version

    @property
    def custom_fields(self):
        """Gets the custom_fields of this IocObject.  # noqa: E501


        :return: The custom_fields of this IocObject.  # noqa: E501
        :rtype: CustomFields
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this IocObject.


        :param custom_fields: The custom_fields of this IocObject.  # noqa: E501
        :type: CustomFields
        """

        self._custom_fields = custom_fields

    @property
    def account(self):
        """Gets the account of this IocObject.  # noqa: E501


        :return: The account of this IocObject.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this IocObject.


        :param account: The account of this IocObject.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def calculated_time(self):
        """Gets the calculated_time of this IocObject.  # noqa: E501

        Do not set the fields bellow this line  # noqa: E501

        :return: The calculated_time of this IocObject.  # noqa: E501
        :rtype: datetime
        """
        return self._calculated_time

    @calculated_time.setter
    def calculated_time(self, calculated_time):
        """Sets the calculated_time of this IocObject.

        Do not set the fields bellow this line  # noqa: E501

        :param calculated_time: The calculated_time of this IocObject.  # noqa: E501
        :type: datetime
        """

        self._calculated_time = calculated_time

    @property
    def comment(self):
        """Gets the comment of this IocObject.  # noqa: E501


        :return: The comment of this IocObject.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this IocObject.


        :param comment: The comment of this IocObject.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def comments(self):
        """Gets the comments of this IocObject.  # noqa: E501


        :return: The comments of this IocObject.  # noqa: E501
        :rtype: Comments
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this IocObject.


        :param comments: The comments of this IocObject.  # noqa: E501
        :type: Comments
        """

        self._comments = comments

    @property
    def first_seen(self):
        """Gets the first_seen of this IocObject.  # noqa: E501


        :return: The first_seen of this IocObject.  # noqa: E501
        :rtype: datetime
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """Sets the first_seen of this IocObject.


        :param first_seen: The first_seen of this IocObject.  # noqa: E501
        :type: datetime
        """

        self._first_seen = first_seen

    @property
    def first_seen_entry_id(self):
        """Gets the first_seen_entry_id of this IocObject.  # noqa: E501


        :return: The first_seen_entry_id of this IocObject.  # noqa: E501
        :rtype: str
        """
        return self._first_seen_entry_id

    @first_seen_entry_id.setter
    def first_seen_entry_id(self, first_seen_entry_id):
        """Sets the first_seen_entry_id of this IocObject.


        :param first_seen_entry_id: The first_seen_entry_id of this IocObject.  # noqa: E501
        :type: str
        """

        self._first_seen_entry_id = first_seen_entry_id

    @property
    def id(self):
        """Gets the id of this IocObject.  # noqa: E501


        :return: The id of this IocObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IocObject.


        :param id: The id of this IocObject.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def indicator_type(self):
        """Gets the indicator_type of this IocObject.  # noqa: E501


        :return: The indicator_type of this IocObject.  # noqa: E501
        :rtype: str
        """
        return self._indicator_type

    @indicator_type.setter
    def indicator_type(self, indicator_type):
        """Sets the indicator_type of this IocObject.


        :param indicator_type: The indicator_type of this IocObject.  # noqa: E501
        :type: str
        """

        self._indicator_type = indicator_type

    @property
    def insight_cache(self):
        """Gets the insight_cache of this IocObject.  # noqa: E501


        :return: The insight_cache of this IocObject.  # noqa: E501
        :rtype: InsightCache
        """
        return self._insight_cache

    @insight_cache.setter
    def insight_cache(self, insight_cache):
        """Sets the insight_cache of this IocObject.


        :param insight_cache: The insight_cache of this IocObject.  # noqa: E501
        :type: InsightCache
        """

        self._insight_cache = insight_cache

    @property
    def investigation_i_ds(self):
        """Gets the investigation_i_ds of this IocObject.  # noqa: E501


        :return: The investigation_i_ds of this IocObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._investigation_i_ds

    @investigation_i_ds.setter
    def investigation_i_ds(self, investigation_i_ds):
        """Sets the investigation_i_ds of this IocObject.


        :param investigation_i_ds: The investigation_i_ds of this IocObject.  # noqa: E501
        :type: list[str]
        """

        self._investigation_i_ds = investigation_i_ds

    @property
    def last_reputation_run(self):
        """Gets the last_reputation_run of this IocObject.  # noqa: E501


        :return: The last_reputation_run of this IocObject.  # noqa: E501
        :rtype: datetime
        """
        return self._last_reputation_run

    @last_reputation_run.setter
    def last_reputation_run(self, last_reputation_run):
        """Sets the last_reputation_run of this IocObject.


        :param last_reputation_run: The last_reputation_run of this IocObject.  # noqa: E501
        :type: datetime
        """

        self._last_reputation_run = last_reputation_run

    @property
    def last_seen(self):
        """Gets the last_seen of this IocObject.  # noqa: E501


        :return: The last_seen of this IocObject.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this IocObject.


        :param last_seen: The last_seen of this IocObject.  # noqa: E501
        :type: datetime
        """

        self._last_seen = last_seen

    @property
    def last_seen_entry_id(self):
        """Gets the last_seen_entry_id of this IocObject.  # noqa: E501


        :return: The last_seen_entry_id of this IocObject.  # noqa: E501
        :rtype: str
        """
        return self._last_seen_entry_id

    @last_seen_entry_id.setter
    def last_seen_entry_id(self, last_seen_entry_id):
        """Sets the last_seen_entry_id of this IocObject.


        :param last_seen_entry_id: The last_seen_entry_id of this IocObject.  # noqa: E501
        :type: str
        """

        self._last_seen_entry_id = last_seen_entry_id

    @property
    def manual_score(self):
        """Gets the manual_score of this IocObject.  # noqa: E501


        :return: The manual_score of this IocObject.  # noqa: E501
        :rtype: bool
        """
        return self._manual_score

    @manual_score.setter
    def manual_score(self, manual_score):
        """Sets the manual_score of this IocObject.


        :param manual_score: The manual_score of this IocObject.  # noqa: E501
        :type: bool
        """

        self._manual_score = manual_score

    @property
    def manual_set_time(self):
        """Gets the manual_set_time of this IocObject.  # noqa: E501


        :return: The manual_set_time of this IocObject.  # noqa: E501
        :rtype: datetime
        """
        return self._manual_set_time

    @manual_set_time.setter
    def manual_set_time(self, manual_set_time):
        """Sets the manual_set_time of this IocObject.


        :param manual_set_time: The manual_set_time of this IocObject.  # noqa: E501
        :type: datetime
        """

        self._manual_set_time = manual_set_time

    @property
    def manually_edited_fields(self):
        """Gets the manually_edited_fields of this IocObject.  # noqa: E501


        :return: The manually_edited_fields of this IocObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._manually_edited_fields

    @manually_edited_fields.setter
    def manually_edited_fields(self, manually_edited_fields):
        """Sets the manually_edited_fields of this IocObject.


        :param manually_edited_fields: The manually_edited_fields of this IocObject.  # noqa: E501
        :type: list[str]
        """

        self._manually_edited_fields = manually_edited_fields

    @property
    def modified(self):
        """Gets the modified of this IocObject.  # noqa: E501


        :return: The modified of this IocObject.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this IocObject.


        :param modified: The modified of this IocObject.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def modified_time(self):
        """Gets the modified_time of this IocObject.  # noqa: E501


        :return: The modified_time of this IocObject.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this IocObject.


        :param modified_time: The modified_time of this IocObject.  # noqa: E501
        :type: datetime
        """

        self._modified_time = modified_time

    @property
    def module_to_feed_map(self):
        """Gets the module_to_feed_map of this IocObject.  # noqa: E501


        :return: The module_to_feed_map of this IocObject.  # noqa: E501
        :rtype: dict(str, FeedIndicator)
        """
        return self._module_to_feed_map

    @module_to_feed_map.setter
    def module_to_feed_map(self, module_to_feed_map):
        """Sets the module_to_feed_map of this IocObject.


        :param module_to_feed_map: The module_to_feed_map of this IocObject.  # noqa: E501
        :type: dict(str, FeedIndicator)
        """

        self._module_to_feed_map = module_to_feed_map

    @property
    def score(self):
        """Gets the score of this IocObject.  # noqa: E501


        :return: The score of this IocObject.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this IocObject.


        :param score: The score of this IocObject.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def set_by(self):
        """Gets the set_by of this IocObject.  # noqa: E501


        :return: The set_by of this IocObject.  # noqa: E501
        :rtype: str
        """
        return self._set_by

    @set_by.setter
    def set_by(self, set_by):
        """Sets the set_by of this IocObject.


        :param set_by: The set_by of this IocObject.  # noqa: E501
        :type: str
        """

        self._set_by = set_by

    @property
    def sort_values(self):
        """Gets the sort_values of this IocObject.  # noqa: E501


        :return: The sort_values of this IocObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._sort_values

    @sort_values.setter
    def sort_values(self, sort_values):
        """Sets the sort_values of this IocObject.


        :param sort_values: The sort_values of this IocObject.  # noqa: E501
        :type: list[str]
        """

        self._sort_values = sort_values

    @property
    def source(self):
        """Gets the source of this IocObject.  # noqa: E501


        :return: The source of this IocObject.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this IocObject.


        :param source: The source of this IocObject.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def source_brands(self):
        """Gets the source_brands of this IocObject.  # noqa: E501


        :return: The source_brands of this IocObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_brands

    @source_brands.setter
    def source_brands(self, source_brands):
        """Sets the source_brands of this IocObject.


        :param source_brands: The source_brands of this IocObject.  # noqa: E501
        :type: list[str]
        """

        self._source_brands = source_brands

    @property
    def source_instances(self):
        """Gets the source_instances of this IocObject.  # noqa: E501


        :return: The source_instances of this IocObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_instances

    @source_instances.setter
    def source_instances(self, source_instances):
        """Sets the source_instances of this IocObject.


        :param source_instances: The source_instances of this IocObject.  # noqa: E501
        :type: list[str]
        """

        self._source_instances = source_instances

    @property
    def timestamp(self):
        """Gets the timestamp of this IocObject.  # noqa: E501


        :return: The timestamp of this IocObject.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this IocObject.


        :param timestamp: The timestamp of this IocObject.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def value(self):
        """Gets the value of this IocObject.  # noqa: E501


        :return: The value of this IocObject.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IocObject.


        :param value: The value of this IocObject.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def version(self):
        """Gets the version of this IocObject.  # noqa: E501


        :return: The version of this IocObject.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IocObject.


        :param version: The version of this IocObject.  # noqa: E501
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
        if issubclass(IocObject, dict):
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
        if not isinstance(other, IocObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
