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

from demisto_client.demisto_api.models.volume_usage_data import VolumeUsageData  # noqa: F401,E501


class Volume(object):
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
        'created_at': 'str',
        'driver': 'str',
        'labels': 'dict(str, str)',
        'mountpoint': 'str',
        'name': 'str',
        'options': 'dict(str, str)',
        'scope': 'str',
        'status': 'dict(str, object)',
        'usage_data': 'VolumeUsageData'
    }

    attribute_map = {
        'created_at': 'CreatedAt',
        'driver': 'Driver',
        'labels': 'Labels',
        'mountpoint': 'Mountpoint',
        'name': 'Name',
        'options': 'Options',
        'scope': 'Scope',
        'status': 'Status',
        'usage_data': 'UsageData'
    }

    def __init__(self, created_at=None, driver=None, labels=None, mountpoint=None, name=None, options=None, scope=None, status=None, usage_data=None):  # noqa: E501
        """Volume - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._driver = None
        self._labels = None
        self._mountpoint = None
        self._name = None
        self._options = None
        self._scope = None
        self._status = None
        self._usage_data = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        self.driver = driver
        self.labels = labels
        self.mountpoint = mountpoint
        self.name = name
        self.options = options
        self.scope = scope
        if status is not None:
            self.status = status
        if usage_data is not None:
            self.usage_data = usage_data

    @property
    def created_at(self):
        """Gets the created_at of this Volume.  # noqa: E501

        Date/Time the volume was created.  # noqa: E501

        :return: The created_at of this Volume.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Volume.

        Date/Time the volume was created.  # noqa: E501

        :param created_at: The created_at of this Volume.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def driver(self):
        """Gets the driver of this Volume.  # noqa: E501

        Name of the volume driver used by the volume.  # noqa: E501

        :return: The driver of this Volume.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this Volume.

        Name of the volume driver used by the volume.  # noqa: E501

        :param driver: The driver of this Volume.  # noqa: E501
        :type: str
        """
        if driver is None:
            raise ValueError("Invalid value for `driver`, must not be `None`")  # noqa: E501

        self._driver = driver

    @property
    def labels(self):
        """Gets the labels of this Volume.  # noqa: E501

        User-defined key/value metadata.  # noqa: E501

        :return: The labels of this Volume.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Volume.

        User-defined key/value metadata.  # noqa: E501

        :param labels: The labels of this Volume.  # noqa: E501
        :type: dict(str, str)
        """
        if labels is None:
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def mountpoint(self):
        """Gets the mountpoint of this Volume.  # noqa: E501

        Mount path of the volume on the host.  # noqa: E501

        :return: The mountpoint of this Volume.  # noqa: E501
        :rtype: str
        """
        return self._mountpoint

    @mountpoint.setter
    def mountpoint(self, mountpoint):
        """Sets the mountpoint of this Volume.

        Mount path of the volume on the host.  # noqa: E501

        :param mountpoint: The mountpoint of this Volume.  # noqa: E501
        :type: str
        """
        if mountpoint is None:
            raise ValueError("Invalid value for `mountpoint`, must not be `None`")  # noqa: E501

        self._mountpoint = mountpoint

    @property
    def name(self):
        """Gets the name of this Volume.  # noqa: E501

        Name of the volume.  # noqa: E501

        :return: The name of this Volume.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Volume.

        Name of the volume.  # noqa: E501

        :param name: The name of this Volume.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def options(self):
        """Gets the options of this Volume.  # noqa: E501

        The driver specific options used when creating the volume.  # noqa: E501

        :return: The options of this Volume.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Volume.

        The driver specific options used when creating the volume.  # noqa: E501

        :param options: The options of this Volume.  # noqa: E501
        :type: dict(str, str)
        """
        if options is None:
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def scope(self):
        """Gets the scope of this Volume.  # noqa: E501

        The level at which the volume exists. Either `global` for cluster-wide, or `local` for machine level.  # noqa: E501

        :return: The scope of this Volume.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Volume.

        The level at which the volume exists. Either `global` for cluster-wide, or `local` for machine level.  # noqa: E501

        :param scope: The scope of this Volume.  # noqa: E501
        :type: str
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def status(self):
        """Gets the status of this Volume.  # noqa: E501

        Low-level details about the volume, provided by the volume driver. Details are returned as a map with key/value pairs: `{\"key\":\"value\",\"key2\":\"value2\"}`.  The `Status` field is optional, and is omitted if the volume driver does not support this feature.  # noqa: E501

        :return: The status of this Volume.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Volume.

        Low-level details about the volume, provided by the volume driver. Details are returned as a map with key/value pairs: `{\"key\":\"value\",\"key2\":\"value2\"}`.  The `Status` field is optional, and is omitted if the volume driver does not support this feature.  # noqa: E501

        :param status: The status of this Volume.  # noqa: E501
        :type: dict(str, object)
        """

        self._status = status

    @property
    def usage_data(self):
        """Gets the usage_data of this Volume.  # noqa: E501


        :return: The usage_data of this Volume.  # noqa: E501
        :rtype: VolumeUsageData
        """
        return self._usage_data

    @usage_data.setter
    def usage_data(self, usage_data):
        """Sets the usage_data of this Volume.


        :param usage_data: The usage_data of this Volume.  # noqa: E501
        :type: VolumeUsageData
        """

        self._usage_data = usage_data

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
        if issubclass(Volume, dict):
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
        if not isinstance(other, Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
