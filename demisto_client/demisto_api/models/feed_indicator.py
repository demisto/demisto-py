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

from demisto_client.demisto_api.models.custom_fields import CustomFields  # noqa: F401,E501
from demisto_client.demisto_api.models.expiration_policy import ExpirationPolicy  # noqa: F401,E501
from demisto_client.demisto_api.models.expiration_source import ExpirationSource  # noqa: F401,E501
from demisto_client.demisto_api.models.feed_indicator_comment import FeedIndicatorComment  # noqa: F401,E501
from demisto_client.demisto_api.models.relationships_api import RelationshipsAPI  # noqa: F401,E501
from demisto_client.demisto_api.models.reliability import Reliability  # noqa: F401,E501


class FeedIndicator(object):
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
        'expiration_source': 'ExpirationSource',
        'bypass_exclusion_list': 'bool',
        'classifier_id': 'str',
        'classifier_version': 'int',
        'comments': 'list[FeedIndicatorComment]',
        'expiration_interval': 'int',
        'expiration_policy': 'ExpirationPolicy',
        'fetch_time': 'datetime',
        'fields': 'CustomFields',
        'is_enrichment': 'bool',
        'mapper_id': 'str',
        'mapper_version': 'int',
        'modified_time': 'datetime',
        'module_id': 'str',
        'raw_json': 'dict(str, object)',
        'relationships': 'RelationshipsAPI',
        'reliability': 'Reliability',
        'score': 'int',
        'source_brand': 'str',
        'source_instance': 'str',
        'timestamp': 'datetime',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'expiration_source': 'ExpirationSource',
        'bypass_exclusion_list': 'bypassExclusionList',
        'classifier_id': 'classifierId',
        'classifier_version': 'classifierVersion',
        'comments': 'comments',
        'expiration_interval': 'expirationInterval',
        'expiration_policy': 'expirationPolicy',
        'fetch_time': 'fetchTime',
        'fields': 'fields',
        'is_enrichment': 'isEnrichment',
        'mapper_id': 'mapperId',
        'mapper_version': 'mapperVersion',
        'modified_time': 'modifiedTime',
        'module_id': 'moduleId',
        'raw_json': 'rawJSON',
        'relationships': 'relationships',
        'reliability': 'reliability',
        'score': 'score',
        'source_brand': 'sourceBrand',
        'source_instance': 'sourceInstance',
        'timestamp': 'timestamp',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, expiration_source=None, bypass_exclusion_list=None, classifier_id=None, classifier_version=None, comments=None, expiration_interval=None, expiration_policy=None, fetch_time=None, fields=None, is_enrichment=None, mapper_id=None, mapper_version=None, modified_time=None, module_id=None, raw_json=None, relationships=None, reliability=None, score=None, source_brand=None, source_instance=None, timestamp=None, type=None, value=None):  # noqa: E501
        """FeedIndicator - a model defined in Swagger"""  # noqa: E501

        self._expiration_source = None
        self._bypass_exclusion_list = None
        self._classifier_id = None
        self._classifier_version = None
        self._comments = None
        self._expiration_interval = None
        self._expiration_policy = None
        self._fetch_time = None
        self._fields = None
        self._is_enrichment = None
        self._mapper_id = None
        self._mapper_version = None
        self._modified_time = None
        self._module_id = None
        self._raw_json = None
        self._relationships = None
        self._reliability = None
        self._score = None
        self._source_brand = None
        self._source_instance = None
        self._timestamp = None
        self._type = None
        self._value = None
        self.discriminator = None

        if expiration_source is not None:
            self.expiration_source = expiration_source
        if bypass_exclusion_list is not None:
            self.bypass_exclusion_list = bypass_exclusion_list
        if classifier_id is not None:
            self.classifier_id = classifier_id
        if classifier_version is not None:
            self.classifier_version = classifier_version
        if comments is not None:
            self.comments = comments
        if expiration_interval is not None:
            self.expiration_interval = expiration_interval
        if expiration_policy is not None:
            self.expiration_policy = expiration_policy
        if fetch_time is not None:
            self.fetch_time = fetch_time
        if fields is not None:
            self.fields = fields
        if is_enrichment is not None:
            self.is_enrichment = is_enrichment
        if mapper_id is not None:
            self.mapper_id = mapper_id
        if mapper_version is not None:
            self.mapper_version = mapper_version
        if modified_time is not None:
            self.modified_time = modified_time
        if module_id is not None:
            self.module_id = module_id
        if raw_json is not None:
            self.raw_json = raw_json
        if relationships is not None:
            self.relationships = relationships
        if reliability is not None:
            self.reliability = reliability
        if score is not None:
            self.score = score
        if source_brand is not None:
            self.source_brand = source_brand
        if source_instance is not None:
            self.source_instance = source_instance
        if timestamp is not None:
            self.timestamp = timestamp
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def expiration_source(self):
        """Gets the expiration_source of this FeedIndicator.  # noqa: E501


        :return: The expiration_source of this FeedIndicator.  # noqa: E501
        :rtype: ExpirationSource
        """
        return self._expiration_source

    @expiration_source.setter
    def expiration_source(self, expiration_source):
        """Sets the expiration_source of this FeedIndicator.


        :param expiration_source: The expiration_source of this FeedIndicator.  # noqa: E501
        :type: ExpirationSource
        """

        self._expiration_source = expiration_source

    @property
    def bypass_exclusion_list(self):
        """Gets the bypass_exclusion_list of this FeedIndicator.  # noqa: E501


        :return: The bypass_exclusion_list of this FeedIndicator.  # noqa: E501
        :rtype: bool
        """
        return self._bypass_exclusion_list

    @bypass_exclusion_list.setter
    def bypass_exclusion_list(self, bypass_exclusion_list):
        """Sets the bypass_exclusion_list of this FeedIndicator.


        :param bypass_exclusion_list: The bypass_exclusion_list of this FeedIndicator.  # noqa: E501
        :type: bool
        """

        self._bypass_exclusion_list = bypass_exclusion_list

    @property
    def classifier_id(self):
        """Gets the classifier_id of this FeedIndicator.  # noqa: E501


        :return: The classifier_id of this FeedIndicator.  # noqa: E501
        :rtype: str
        """
        return self._classifier_id

    @classifier_id.setter
    def classifier_id(self, classifier_id):
        """Sets the classifier_id of this FeedIndicator.


        :param classifier_id: The classifier_id of this FeedIndicator.  # noqa: E501
        :type: str
        """

        self._classifier_id = classifier_id

    @property
    def classifier_version(self):
        """Gets the classifier_version of this FeedIndicator.  # noqa: E501


        :return: The classifier_version of this FeedIndicator.  # noqa: E501
        :rtype: int
        """
        return self._classifier_version

    @classifier_version.setter
    def classifier_version(self, classifier_version):
        """Sets the classifier_version of this FeedIndicator.


        :param classifier_version: The classifier_version of this FeedIndicator.  # noqa: E501
        :type: int
        """

        self._classifier_version = classifier_version

    @property
    def comments(self):
        """Gets the comments of this FeedIndicator.  # noqa: E501


        :return: The comments of this FeedIndicator.  # noqa: E501
        :rtype: list[FeedIndicatorComment]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this FeedIndicator.


        :param comments: The comments of this FeedIndicator.  # noqa: E501
        :type: list[FeedIndicatorComment]
        """

        self._comments = comments

    @property
    def expiration_interval(self):
        """Gets the expiration_interval of this FeedIndicator.  # noqa: E501


        :return: The expiration_interval of this FeedIndicator.  # noqa: E501
        :rtype: int
        """
        return self._expiration_interval

    @expiration_interval.setter
    def expiration_interval(self, expiration_interval):
        """Sets the expiration_interval of this FeedIndicator.


        :param expiration_interval: The expiration_interval of this FeedIndicator.  # noqa: E501
        :type: int
        """

        self._expiration_interval = expiration_interval

    @property
    def expiration_policy(self):
        """Gets the expiration_policy of this FeedIndicator.  # noqa: E501


        :return: The expiration_policy of this FeedIndicator.  # noqa: E501
        :rtype: ExpirationPolicy
        """
        return self._expiration_policy

    @expiration_policy.setter
    def expiration_policy(self, expiration_policy):
        """Sets the expiration_policy of this FeedIndicator.


        :param expiration_policy: The expiration_policy of this FeedIndicator.  # noqa: E501
        :type: ExpirationPolicy
        """

        self._expiration_policy = expiration_policy

    @property
    def fetch_time(self):
        """Gets the fetch_time of this FeedIndicator.  # noqa: E501


        :return: The fetch_time of this FeedIndicator.  # noqa: E501
        :rtype: datetime
        """
        return self._fetch_time

    @fetch_time.setter
    def fetch_time(self, fetch_time):
        """Sets the fetch_time of this FeedIndicator.


        :param fetch_time: The fetch_time of this FeedIndicator.  # noqa: E501
        :type: datetime
        """

        self._fetch_time = fetch_time

    @property
    def fields(self):
        """Gets the fields of this FeedIndicator.  # noqa: E501


        :return: The fields of this FeedIndicator.  # noqa: E501
        :rtype: CustomFields
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this FeedIndicator.


        :param fields: The fields of this FeedIndicator.  # noqa: E501
        :type: CustomFields
        """

        self._fields = fields

    @property
    def is_enrichment(self):
        """Gets the is_enrichment of this FeedIndicator.  # noqa: E501


        :return: The is_enrichment of this FeedIndicator.  # noqa: E501
        :rtype: bool
        """
        return self._is_enrichment

    @is_enrichment.setter
    def is_enrichment(self, is_enrichment):
        """Sets the is_enrichment of this FeedIndicator.


        :param is_enrichment: The is_enrichment of this FeedIndicator.  # noqa: E501
        :type: bool
        """

        self._is_enrichment = is_enrichment

    @property
    def mapper_id(self):
        """Gets the mapper_id of this FeedIndicator.  # noqa: E501


        :return: The mapper_id of this FeedIndicator.  # noqa: E501
        :rtype: str
        """
        return self._mapper_id

    @mapper_id.setter
    def mapper_id(self, mapper_id):
        """Sets the mapper_id of this FeedIndicator.


        :param mapper_id: The mapper_id of this FeedIndicator.  # noqa: E501
        :type: str
        """

        self._mapper_id = mapper_id

    @property
    def mapper_version(self):
        """Gets the mapper_version of this FeedIndicator.  # noqa: E501


        :return: The mapper_version of this FeedIndicator.  # noqa: E501
        :rtype: int
        """
        return self._mapper_version

    @mapper_version.setter
    def mapper_version(self, mapper_version):
        """Sets the mapper_version of this FeedIndicator.


        :param mapper_version: The mapper_version of this FeedIndicator.  # noqa: E501
        :type: int
        """

        self._mapper_version = mapper_version

    @property
    def modified_time(self):
        """Gets the modified_time of this FeedIndicator.  # noqa: E501


        :return: The modified_time of this FeedIndicator.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this FeedIndicator.


        :param modified_time: The modified_time of this FeedIndicator.  # noqa: E501
        :type: datetime
        """

        self._modified_time = modified_time

    @property
    def module_id(self):
        """Gets the module_id of this FeedIndicator.  # noqa: E501


        :return: The module_id of this FeedIndicator.  # noqa: E501
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this FeedIndicator.


        :param module_id: The module_id of this FeedIndicator.  # noqa: E501
        :type: str
        """

        self._module_id = module_id

    @property
    def raw_json(self):
        """Gets the raw_json of this FeedIndicator.  # noqa: E501


        :return: The raw_json of this FeedIndicator.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._raw_json

    @raw_json.setter
    def raw_json(self, raw_json):
        """Sets the raw_json of this FeedIndicator.


        :param raw_json: The raw_json of this FeedIndicator.  # noqa: E501
        :type: dict(str, object)
        """

        self._raw_json = raw_json

    @property
    def relationships(self):
        """Gets the relationships of this FeedIndicator.  # noqa: E501


        :return: The relationships of this FeedIndicator.  # noqa: E501
        :rtype: RelationshipsAPI
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this FeedIndicator.


        :param relationships: The relationships of this FeedIndicator.  # noqa: E501
        :type: RelationshipsAPI
        """

        self._relationships = relationships

    @property
    def reliability(self):
        """Gets the reliability of this FeedIndicator.  # noqa: E501


        :return: The reliability of this FeedIndicator.  # noqa: E501
        :rtype: Reliability
        """
        return self._reliability

    @reliability.setter
    def reliability(self, reliability):
        """Sets the reliability of this FeedIndicator.


        :param reliability: The reliability of this FeedIndicator.  # noqa: E501
        :type: Reliability
        """

        self._reliability = reliability

    @property
    def score(self):
        """Gets the score of this FeedIndicator.  # noqa: E501


        :return: The score of this FeedIndicator.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this FeedIndicator.


        :param score: The score of this FeedIndicator.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def source_brand(self):
        """Gets the source_brand of this FeedIndicator.  # noqa: E501


        :return: The source_brand of this FeedIndicator.  # noqa: E501
        :rtype: str
        """
        return self._source_brand

    @source_brand.setter
    def source_brand(self, source_brand):
        """Sets the source_brand of this FeedIndicator.


        :param source_brand: The source_brand of this FeedIndicator.  # noqa: E501
        :type: str
        """

        self._source_brand = source_brand

    @property
    def source_instance(self):
        """Gets the source_instance of this FeedIndicator.  # noqa: E501


        :return: The source_instance of this FeedIndicator.  # noqa: E501
        :rtype: str
        """
        return self._source_instance

    @source_instance.setter
    def source_instance(self, source_instance):
        """Sets the source_instance of this FeedIndicator.


        :param source_instance: The source_instance of this FeedIndicator.  # noqa: E501
        :type: str
        """

        self._source_instance = source_instance

    @property
    def timestamp(self):
        """Gets the timestamp of this FeedIndicator.  # noqa: E501


        :return: The timestamp of this FeedIndicator.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this FeedIndicator.


        :param timestamp: The timestamp of this FeedIndicator.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this FeedIndicator.  # noqa: E501


        :return: The type of this FeedIndicator.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FeedIndicator.


        :param type: The type of this FeedIndicator.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this FeedIndicator.  # noqa: E501


        :return: The value of this FeedIndicator.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FeedIndicator.


        :param value: The value of this FeedIndicator.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(FeedIndicator, dict):
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
        if not isinstance(other, FeedIndicator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
