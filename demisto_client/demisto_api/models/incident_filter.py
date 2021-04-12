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

from demisto_client.demisto_api.models.duration import Duration  # noqa: F401,E501
from demisto_client.demisto_api.models.incident_status import IncidentStatus  # noqa: F401,E501
from demisto_client.demisto_api.models.incident_wrapper import IncidentWrapper  # noqa: F401,E501
from demisto_client.demisto_api.models.order import Order  # noqa: F401,E501
from demisto_client.demisto_api.models.period import Period  # noqa: F401,E501
from demisto_client.demisto_api.models.severity import Severity  # noqa: F401,E501


class IncidentFilter(object):
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
        'cache': 'dict(str, list[str])',
        'and_op': 'bool',
        'category': 'list[str]',
        'details': 'str',
        'files': 'list[str]',
        'first_incident_in_page': 'IncidentWrapper',
        'from_activated_date': 'datetime',
        'from_closed_date': 'datetime',
        'from_date': 'datetime',
        'from_date_license': 'datetime',
        'from_due_date': 'datetime',
        'from_reminder': 'datetime',
        'id': 'list[str]',
        'include_tmp': 'bool',
        'investigation': 'list[str]',
        'last_incident_in_page': 'IncidentWrapper',
        'level': 'list[Severity]',
        'name': 'list[str]',
        'next_page': 'bool',
        'not_category': 'list[str]',
        'not_investigation': 'list[str]',
        'not_status': 'list[IncidentStatus]',
        'page': 'int',
        'parent': 'list[str]',
        'period': 'Period',
        'query': 'str',
        'reason': 'list[str]',
        'search_after': 'list[str]',
        'search_before': 'list[str]',
        'sequential_pages_search': 'bool',
        'size': 'int',
        'sort': 'list[Order]',
        'status': 'list[IncidentStatus]',
        'systems': 'list[str]',
        'time_frame': 'Duration',
        'to_activated_date': 'datetime',
        'to_closed_date': 'datetime',
        'to_date': 'datetime',
        'to_due_date': 'datetime',
        'to_reminder': 'datetime',
        'total_only': 'bool',
        'type': 'list[str]',
        'urls': 'list[str]',
        'users': 'list[str]'
    }

    attribute_map = {
        'cache': 'Cache',
        'and_op': 'andOp',
        'category': 'category',
        'details': 'details',
        'files': 'files',
        'first_incident_in_page': 'firstIncidentInPage',
        'from_activated_date': 'fromActivatedDate',
        'from_closed_date': 'fromClosedDate',
        'from_date': 'fromDate',
        'from_date_license': 'fromDateLicense',
        'from_due_date': 'fromDueDate',
        'from_reminder': 'fromReminder',
        'id': 'id',
        'include_tmp': 'includeTmp',
        'investigation': 'investigation',
        'last_incident_in_page': 'lastIncidentInPage',
        'level': 'level',
        'name': 'name',
        'next_page': 'nextPage',
        'not_category': 'notCategory',
        'not_investigation': 'notInvestigation',
        'not_status': 'notStatus',
        'page': 'page',
        'parent': 'parent',
        'period': 'period',
        'query': 'query',
        'reason': 'reason',
        'search_after': 'searchAfter',
        'search_before': 'searchBefore',
        'sequential_pages_search': 'sequentialPagesSearch',
        'size': 'size',
        'sort': 'sort',
        'status': 'status',
        'systems': 'systems',
        'time_frame': 'timeFrame',
        'to_activated_date': 'toActivatedDate',
        'to_closed_date': 'toClosedDate',
        'to_date': 'toDate',
        'to_due_date': 'toDueDate',
        'to_reminder': 'toReminder',
        'total_only': 'totalOnly',
        'type': 'type',
        'urls': 'urls',
        'users': 'users'
    }

    def __init__(self, cache=None, and_op=None, category=None, details=None, files=None, first_incident_in_page=None, from_activated_date=None, from_closed_date=None, from_date=None, from_date_license=None, from_due_date=None, from_reminder=None, id=None, include_tmp=None, investigation=None, last_incident_in_page=None, level=None, name=None, next_page=None, not_category=None, not_investigation=None, not_status=None, page=None, parent=None, period=None, query=None, reason=None, search_after=None, search_before=None, sequential_pages_search=None, size=None, sort=None, status=None, systems=None, time_frame=None, to_activated_date=None, to_closed_date=None, to_date=None, to_due_date=None, to_reminder=None, total_only=None, type=None, urls=None, users=None):  # noqa: E501
        """IncidentFilter - a model defined in Swagger"""  # noqa: E501

        self._cache = None
        self._and_op = None
        self._category = None
        self._details = None
        self._files = None
        self._first_incident_in_page = None
        self._from_activated_date = None
        self._from_closed_date = None
        self._from_date = None
        self._from_date_license = None
        self._from_due_date = None
        self._from_reminder = None
        self._id = None
        self._include_tmp = None
        self._investigation = None
        self._last_incident_in_page = None
        self._level = None
        self._name = None
        self._next_page = None
        self._not_category = None
        self._not_investigation = None
        self._not_status = None
        self._page = None
        self._parent = None
        self._period = None
        self._query = None
        self._reason = None
        self._search_after = None
        self._search_before = None
        self._sequential_pages_search = None
        self._size = None
        self._sort = None
        self._status = None
        self._systems = None
        self._time_frame = None
        self._to_activated_date = None
        self._to_closed_date = None
        self._to_date = None
        self._to_due_date = None
        self._to_reminder = None
        self._total_only = None
        self._type = None
        self._urls = None
        self._users = None
        self.discriminator = None

        if cache is not None:
            self.cache = cache
        if and_op is not None:
            self.and_op = and_op
        if category is not None:
            self.category = category
        if details is not None:
            self.details = details
        if files is not None:
            self.files = files
        if first_incident_in_page is not None:
            self.first_incident_in_page = first_incident_in_page
        if from_activated_date is not None:
            self.from_activated_date = from_activated_date
        if from_closed_date is not None:
            self.from_closed_date = from_closed_date
        if from_date is not None:
            self.from_date = from_date
        if from_date_license is not None:
            self.from_date_license = from_date_license
        if from_due_date is not None:
            self.from_due_date = from_due_date
        if from_reminder is not None:
            self.from_reminder = from_reminder
        if id is not None:
            self.id = id
        if include_tmp is not None:
            self.include_tmp = include_tmp
        if investigation is not None:
            self.investigation = investigation
        if last_incident_in_page is not None:
            self.last_incident_in_page = last_incident_in_page
        if level is not None:
            self.level = level
        if name is not None:
            self.name = name
        if next_page is not None:
            self.next_page = next_page
        if not_category is not None:
            self.not_category = not_category
        if not_investigation is not None:
            self.not_investigation = not_investigation
        if not_status is not None:
            self.not_status = not_status
        if page is not None:
            self.page = page
        if parent is not None:
            self.parent = parent
        if period is not None:
            self.period = period
        if query is not None:
            self.query = query
        if reason is not None:
            self.reason = reason
        if search_after is not None:
            self.search_after = search_after
        if search_before is not None:
            self.search_before = search_before
        if sequential_pages_search is not None:
            self.sequential_pages_search = sequential_pages_search
        if size is not None:
            self.size = size
        if sort is not None:
            self.sort = sort
        if status is not None:
            self.status = status
        if systems is not None:
            self.systems = systems
        if time_frame is not None:
            self.time_frame = time_frame
        if to_activated_date is not None:
            self.to_activated_date = to_activated_date
        if to_closed_date is not None:
            self.to_closed_date = to_closed_date
        if to_date is not None:
            self.to_date = to_date
        if to_due_date is not None:
            self.to_due_date = to_due_date
        if to_reminder is not None:
            self.to_reminder = to_reminder
        if total_only is not None:
            self.total_only = total_only
        if type is not None:
            self.type = type
        if urls is not None:
            self.urls = urls
        if users is not None:
            self.users = users

    @property
    def cache(self):
        """Gets the cache of this IncidentFilter.  # noqa: E501

        Cache of join functions  # noqa: E501

        :return: The cache of this IncidentFilter.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._cache

    @cache.setter
    def cache(self, cache):
        """Sets the cache of this IncidentFilter.

        Cache of join functions  # noqa: E501

        :param cache: The cache of this IncidentFilter.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._cache = cache

    @property
    def and_op(self):
        """Gets the and_op of this IncidentFilter.  # noqa: E501


        :return: The and_op of this IncidentFilter.  # noqa: E501
        :rtype: bool
        """
        return self._and_op

    @and_op.setter
    def and_op(self, and_op):
        """Sets the and_op of this IncidentFilter.


        :param and_op: The and_op of this IncidentFilter.  # noqa: E501
        :type: bool
        """

        self._and_op = and_op

    @property
    def category(self):
        """Gets the category of this IncidentFilter.  # noqa: E501


        :return: The category of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this IncidentFilter.


        :param category: The category of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._category = category

    @property
    def details(self):
        """Gets the details of this IncidentFilter.  # noqa: E501


        :return: The details of this IncidentFilter.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this IncidentFilter.


        :param details: The details of this IncidentFilter.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def files(self):
        """Gets the files of this IncidentFilter.  # noqa: E501


        :return: The files of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this IncidentFilter.


        :param files: The files of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._files = files

    @property
    def first_incident_in_page(self):
        """Gets the first_incident_in_page of this IncidentFilter.  # noqa: E501


        :return: The first_incident_in_page of this IncidentFilter.  # noqa: E501
        :rtype: IncidentWrapper
        """
        return self._first_incident_in_page

    @first_incident_in_page.setter
    def first_incident_in_page(self, first_incident_in_page):
        """Sets the first_incident_in_page of this IncidentFilter.


        :param first_incident_in_page: The first_incident_in_page of this IncidentFilter.  # noqa: E501
        :type: IncidentWrapper
        """

        self._first_incident_in_page = first_incident_in_page

    @property
    def from_activated_date(self):
        """Gets the from_activated_date of this IncidentFilter.  # noqa: E501


        :return: The from_activated_date of this IncidentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._from_activated_date

    @from_activated_date.setter
    def from_activated_date(self, from_activated_date):
        """Sets the from_activated_date of this IncidentFilter.


        :param from_activated_date: The from_activated_date of this IncidentFilter.  # noqa: E501
        :type: datetime
        """

        self._from_activated_date = from_activated_date

    @property
    def from_closed_date(self):
        """Gets the from_closed_date of this IncidentFilter.  # noqa: E501


        :return: The from_closed_date of this IncidentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._from_closed_date

    @from_closed_date.setter
    def from_closed_date(self, from_closed_date):
        """Sets the from_closed_date of this IncidentFilter.


        :param from_closed_date: The from_closed_date of this IncidentFilter.  # noqa: E501
        :type: datetime
        """

        self._from_closed_date = from_closed_date

    @property
    def from_date(self):
        """Gets the from_date of this IncidentFilter.  # noqa: E501


        :return: The from_date of this IncidentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this IncidentFilter.


        :param from_date: The from_date of this IncidentFilter.  # noqa: E501
        :type: datetime
        """

        self._from_date = from_date

    @property
    def from_date_license(self):
        """Gets the from_date_license of this IncidentFilter.  # noqa: E501


        :return: The from_date_license of this IncidentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date_license

    @from_date_license.setter
    def from_date_license(self, from_date_license):
        """Sets the from_date_license of this IncidentFilter.


        :param from_date_license: The from_date_license of this IncidentFilter.  # noqa: E501
        :type: datetime
        """

        self._from_date_license = from_date_license

    @property
    def from_due_date(self):
        """Gets the from_due_date of this IncidentFilter.  # noqa: E501


        :return: The from_due_date of this IncidentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._from_due_date

    @from_due_date.setter
    def from_due_date(self, from_due_date):
        """Sets the from_due_date of this IncidentFilter.


        :param from_due_date: The from_due_date of this IncidentFilter.  # noqa: E501
        :type: datetime
        """

        self._from_due_date = from_due_date

    @property
    def from_reminder(self):
        """Gets the from_reminder of this IncidentFilter.  # noqa: E501


        :return: The from_reminder of this IncidentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._from_reminder

    @from_reminder.setter
    def from_reminder(self, from_reminder):
        """Sets the from_reminder of this IncidentFilter.


        :param from_reminder: The from_reminder of this IncidentFilter.  # noqa: E501
        :type: datetime
        """

        self._from_reminder = from_reminder

    @property
    def id(self):
        """Gets the id of this IncidentFilter.  # noqa: E501


        :return: The id of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IncidentFilter.


        :param id: The id of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._id = id

    @property
    def include_tmp(self):
        """Gets the include_tmp of this IncidentFilter.  # noqa: E501


        :return: The include_tmp of this IncidentFilter.  # noqa: E501
        :rtype: bool
        """
        return self._include_tmp

    @include_tmp.setter
    def include_tmp(self, include_tmp):
        """Sets the include_tmp of this IncidentFilter.


        :param include_tmp: The include_tmp of this IncidentFilter.  # noqa: E501
        :type: bool
        """

        self._include_tmp = include_tmp

    @property
    def investigation(self):
        """Gets the investigation of this IncidentFilter.  # noqa: E501


        :return: The investigation of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._investigation

    @investigation.setter
    def investigation(self, investigation):
        """Sets the investigation of this IncidentFilter.


        :param investigation: The investigation of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._investigation = investigation

    @property
    def last_incident_in_page(self):
        """Gets the last_incident_in_page of this IncidentFilter.  # noqa: E501


        :return: The last_incident_in_page of this IncidentFilter.  # noqa: E501
        :rtype: IncidentWrapper
        """
        return self._last_incident_in_page

    @last_incident_in_page.setter
    def last_incident_in_page(self, last_incident_in_page):
        """Sets the last_incident_in_page of this IncidentFilter.


        :param last_incident_in_page: The last_incident_in_page of this IncidentFilter.  # noqa: E501
        :type: IncidentWrapper
        """

        self._last_incident_in_page = last_incident_in_page

    @property
    def level(self):
        """Gets the level of this IncidentFilter.  # noqa: E501


        :return: The level of this IncidentFilter.  # noqa: E501
        :rtype: list[Severity]
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this IncidentFilter.


        :param level: The level of this IncidentFilter.  # noqa: E501
        :type: list[Severity]
        """

        self._level = level

    @property
    def name(self):
        """Gets the name of this IncidentFilter.  # noqa: E501


        :return: The name of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IncidentFilter.


        :param name: The name of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._name = name

    @property
    def next_page(self):
        """Gets the next_page of this IncidentFilter.  # noqa: E501


        :return: The next_page of this IncidentFilter.  # noqa: E501
        :rtype: bool
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this IncidentFilter.


        :param next_page: The next_page of this IncidentFilter.  # noqa: E501
        :type: bool
        """

        self._next_page = next_page

    @property
    def not_category(self):
        """Gets the not_category of this IncidentFilter.  # noqa: E501


        :return: The not_category of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._not_category

    @not_category.setter
    def not_category(self, not_category):
        """Sets the not_category of this IncidentFilter.


        :param not_category: The not_category of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._not_category = not_category

    @property
    def not_investigation(self):
        """Gets the not_investigation of this IncidentFilter.  # noqa: E501


        :return: The not_investigation of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._not_investigation

    @not_investigation.setter
    def not_investigation(self, not_investigation):
        """Sets the not_investigation of this IncidentFilter.


        :param not_investigation: The not_investigation of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._not_investigation = not_investigation

    @property
    def not_status(self):
        """Gets the not_status of this IncidentFilter.  # noqa: E501


        :return: The not_status of this IncidentFilter.  # noqa: E501
        :rtype: list[IncidentStatus]
        """
        return self._not_status

    @not_status.setter
    def not_status(self, not_status):
        """Sets the not_status of this IncidentFilter.


        :param not_status: The not_status of this IncidentFilter.  # noqa: E501
        :type: list[IncidentStatus]
        """

        self._not_status = not_status

    @property
    def page(self):
        """Gets the page of this IncidentFilter.  # noqa: E501

        0-based page  # noqa: E501

        :return: The page of this IncidentFilter.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this IncidentFilter.

        0-based page  # noqa: E501

        :param page: The page of this IncidentFilter.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def parent(self):
        """Gets the parent of this IncidentFilter.  # noqa: E501


        :return: The parent of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this IncidentFilter.


        :param parent: The parent of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._parent = parent

    @property
    def period(self):
        """Gets the period of this IncidentFilter.  # noqa: E501


        :return: The period of this IncidentFilter.  # noqa: E501
        :rtype: Period
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this IncidentFilter.


        :param period: The period of this IncidentFilter.  # noqa: E501
        :type: Period
        """

        self._period = period

    @property
    def query(self):
        """Gets the query of this IncidentFilter.  # noqa: E501


        :return: The query of this IncidentFilter.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this IncidentFilter.


        :param query: The query of this IncidentFilter.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def reason(self):
        """Gets the reason of this IncidentFilter.  # noqa: E501


        :return: The reason of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this IncidentFilter.


        :param reason: The reason of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._reason = reason

    @property
    def search_after(self):
        """Gets the search_after of this IncidentFilter.  # noqa: E501

        Efficient next page, pass max sort value from previous page  # noqa: E501

        :return: The search_after of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_after

    @search_after.setter
    def search_after(self, search_after):
        """Sets the search_after of this IncidentFilter.

        Efficient next page, pass max sort value from previous page  # noqa: E501

        :param search_after: The search_after of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._search_after = search_after

    @property
    def search_before(self):
        """Gets the search_before of this IncidentFilter.  # noqa: E501

        Efficient prev page, pass min sort value from next page  # noqa: E501

        :return: The search_before of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_before

    @search_before.setter
    def search_before(self, search_before):
        """Sets the search_before of this IncidentFilter.

        Efficient prev page, pass min sort value from next page  # noqa: E501

        :param search_before: The search_before of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._search_before = search_before

    @property
    def sequential_pages_search(self):
        """Gets the sequential_pages_search of this IncidentFilter.  # noqa: E501


        :return: The sequential_pages_search of this IncidentFilter.  # noqa: E501
        :rtype: bool
        """
        return self._sequential_pages_search

    @sequential_pages_search.setter
    def sequential_pages_search(self, sequential_pages_search):
        """Sets the sequential_pages_search of this IncidentFilter.


        :param sequential_pages_search: The sequential_pages_search of this IncidentFilter.  # noqa: E501
        :type: bool
        """

        self._sequential_pages_search = sequential_pages_search

    @property
    def size(self):
        """Gets the size of this IncidentFilter.  # noqa: E501

        Size is limited to 1000, if not passed it defaults to 0, and no results will return  # noqa: E501

        :return: The size of this IncidentFilter.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this IncidentFilter.

        Size is limited to 1000, if not passed it defaults to 0, and no results will return  # noqa: E501

        :param size: The size of this IncidentFilter.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def sort(self):
        """Gets the sort of this IncidentFilter.  # noqa: E501

        The sort order  # noqa: E501

        :return: The sort of this IncidentFilter.  # noqa: E501
        :rtype: list[Order]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this IncidentFilter.

        The sort order  # noqa: E501

        :param sort: The sort of this IncidentFilter.  # noqa: E501
        :type: list[Order]
        """

        self._sort = sort

    @property
    def status(self):
        """Gets the status of this IncidentFilter.  # noqa: E501


        :return: The status of this IncidentFilter.  # noqa: E501
        :rtype: list[IncidentStatus]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IncidentFilter.


        :param status: The status of this IncidentFilter.  # noqa: E501
        :type: list[IncidentStatus]
        """

        self._status = status

    @property
    def systems(self):
        """Gets the systems of this IncidentFilter.  # noqa: E501


        :return: The systems of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """Sets the systems of this IncidentFilter.


        :param systems: The systems of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._systems = systems

    @property
    def time_frame(self):
        """Gets the time_frame of this IncidentFilter.  # noqa: E501


        :return: The time_frame of this IncidentFilter.  # noqa: E501
        :rtype: Duration
        """
        return self._time_frame

    @time_frame.setter
    def time_frame(self, time_frame):
        """Sets the time_frame of this IncidentFilter.


        :param time_frame: The time_frame of this IncidentFilter.  # noqa: E501
        :type: Duration
        """

        self._time_frame = time_frame

    @property
    def to_activated_date(self):
        """Gets the to_activated_date of this IncidentFilter.  # noqa: E501


        :return: The to_activated_date of this IncidentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._to_activated_date

    @to_activated_date.setter
    def to_activated_date(self, to_activated_date):
        """Sets the to_activated_date of this IncidentFilter.


        :param to_activated_date: The to_activated_date of this IncidentFilter.  # noqa: E501
        :type: datetime
        """

        self._to_activated_date = to_activated_date

    @property
    def to_closed_date(self):
        """Gets the to_closed_date of this IncidentFilter.  # noqa: E501


        :return: The to_closed_date of this IncidentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._to_closed_date

    @to_closed_date.setter
    def to_closed_date(self, to_closed_date):
        """Sets the to_closed_date of this IncidentFilter.


        :param to_closed_date: The to_closed_date of this IncidentFilter.  # noqa: E501
        :type: datetime
        """

        self._to_closed_date = to_closed_date

    @property
    def to_date(self):
        """Gets the to_date of this IncidentFilter.  # noqa: E501


        :return: The to_date of this IncidentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this IncidentFilter.


        :param to_date: The to_date of this IncidentFilter.  # noqa: E501
        :type: datetime
        """

        self._to_date = to_date

    @property
    def to_due_date(self):
        """Gets the to_due_date of this IncidentFilter.  # noqa: E501


        :return: The to_due_date of this IncidentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._to_due_date

    @to_due_date.setter
    def to_due_date(self, to_due_date):
        """Sets the to_due_date of this IncidentFilter.


        :param to_due_date: The to_due_date of this IncidentFilter.  # noqa: E501
        :type: datetime
        """

        self._to_due_date = to_due_date

    @property
    def to_reminder(self):
        """Gets the to_reminder of this IncidentFilter.  # noqa: E501


        :return: The to_reminder of this IncidentFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._to_reminder

    @to_reminder.setter
    def to_reminder(self, to_reminder):
        """Sets the to_reminder of this IncidentFilter.


        :param to_reminder: The to_reminder of this IncidentFilter.  # noqa: E501
        :type: datetime
        """

        self._to_reminder = to_reminder

    @property
    def total_only(self):
        """Gets the total_only of this IncidentFilter.  # noqa: E501


        :return: The total_only of this IncidentFilter.  # noqa: E501
        :rtype: bool
        """
        return self._total_only

    @total_only.setter
    def total_only(self, total_only):
        """Sets the total_only of this IncidentFilter.


        :param total_only: The total_only of this IncidentFilter.  # noqa: E501
        :type: bool
        """

        self._total_only = total_only

    @property
    def type(self):
        """Gets the type of this IncidentFilter.  # noqa: E501


        :return: The type of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IncidentFilter.


        :param type: The type of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def urls(self):
        """Gets the urls of this IncidentFilter.  # noqa: E501


        :return: The urls of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this IncidentFilter.


        :param urls: The urls of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._urls = urls

    @property
    def users(self):
        """Gets the users of this IncidentFilter.  # noqa: E501


        :return: The users of this IncidentFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this IncidentFilter.


        :param users: The users of this IncidentFilter.  # noqa: E501
        :type: list[str]
        """

        self._users = users

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
        if issubclass(IncidentFilter, dict):
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
        if not isinstance(other, IncidentFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
