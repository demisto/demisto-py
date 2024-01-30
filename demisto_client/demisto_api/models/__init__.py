# coding: utf-8

"""
    Demisto API

    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from demisto_client.demisto_api.models.advance_arg import AdvanceArg
from demisto_client.demisto_api.models.arg_atomic_filter import ArgAtomicFilter
from demisto_client.demisto_api.models.arg_filter import ArgFilter
from demisto_client.demisto_api.models.arg_transformer import ArgTransformer
from demisto_client.demisto_api.models.argument import Argument
from demisto_client.demisto_api.models.array_positions import ArrayPositions
from demisto_client.demisto_api.models.attachment import Attachment
from demisto_client.demisto_api.models.audit import Audit
from demisto_client.demisto_api.models.audit_result import AuditResult
from demisto_client.demisto_api.models.automation_script import AutomationScript
from demisto_client.demisto_api.models.automation_script_api import AutomationScriptAPI
from demisto_client.demisto_api.models.automation_script_filter import AutomationScriptFilter
from demisto_client.demisto_api.models.automation_script_filter_wrapper import AutomationScriptFilterWrapper
from demisto_client.demisto_api.models.automation_script_result import AutomationScriptResult
from demisto_client.demisto_api.models.command import Command
from demisto_client.demisto_api.models.common_fields import CommonFields
from demisto_client.demisto_api.models.complex_arg import ComplexArg
from demisto_client.demisto_api.models.config_data_type import ConfigDataType
from demisto_client.demisto_api.models.config_field import ConfigField
from demisto_client.demisto_api.models.create_incident_request import CreateIncidentRequest
from demisto_client.demisto_api.models.custom_fields import CustomFields
from demisto_client.demisto_api.models.d_bot_score import DBotScore
from demisto_client.demisto_api.models.dashboard import Dashboard
from demisto_client.demisto_api.models.data_collection_form import DataCollectionForm
from demisto_client.demisto_api.models.date_range import DateRange
from demisto_client.demisto_api.models.date_range_filter import DateRangeFilter
from demisto_client.demisto_api.models.delete_evidence import DeleteEvidence
from demisto_client.demisto_api.models.docker_image import DockerImage
from demisto_client.demisto_api.models.docker_images_result import DockerImagesResult
from demisto_client.demisto_api.models.download_entry import DownloadEntry
from demisto_client.demisto_api.models.duration import Duration
from demisto_client.demisto_api.models.ending_type import EndingType
from demisto_client.demisto_api.models.entry import Entry
from demisto_client.demisto_api.models.entry_category import EntryCategory
from demisto_client.demisto_api.models.entry_history import EntryHistory
from demisto_client.demisto_api.models.entry_reputation import EntryReputation
from demisto_client.demisto_api.models.entry_task import EntryTask
from demisto_client.demisto_api.models.entry_type import EntryType
from demisto_client.demisto_api.models.evidence import Evidence
from demisto_client.demisto_api.models.evidence_data import EvidenceData
from demisto_client.demisto_api.models.evidences import Evidences
from demisto_client.demisto_api.models.evidences_filter_wrapper import EvidencesFilterWrapper
from demisto_client.demisto_api.models.evidences_search_response import EvidencesSearchResponse
from demisto_client.demisto_api.models.expiration_policy import ExpirationPolicy
from demisto_client.demisto_api.models.expiration_settings_source import ExpirationSettingsSource
from demisto_client.demisto_api.models.expiration_source import ExpirationSource
from demisto_client.demisto_api.models.feed_indicator import FeedIndicator
from demisto_client.demisto_api.models.feed_indicators import FeedIndicators
from demisto_client.demisto_api.models.feed_indicators_request import FeedIndicatorsRequest
from demisto_client.demisto_api.models.field_group import FieldGroup
from demisto_client.demisto_api.models.field_mapping import FieldMapping
from demisto_client.demisto_api.models.field_term_location_map import FieldTermLocationMap
from demisto_client.demisto_api.models.file_metadata import FileMetadata
from demisto_client.demisto_api.models.filter_cache import FilterCache
from demisto_client.demisto_api.models.filter_operator_id import FilterOperatorID
from demisto_client.demisto_api.models.form_display import FormDisplay
from demisto_client.demisto_api.models.generic_indicator_update_batch import GenericIndicatorUpdateBatch
from demisto_client.demisto_api.models.generic_string_date_filter import GenericStringDateFilter
from demisto_client.demisto_api.models.generic_string_filter import GenericStringFilter
from demisto_client.demisto_api.models.grid_column import GridColumn
from demisto_client.demisto_api.models.group import Group
from demisto_client.demisto_api.models.groups import Groups
from demisto_client.demisto_api.models.human_cron import HumanCron
from demisto_client.demisto_api.models.important import Important
from demisto_client.demisto_api.models.incident import Incident
from demisto_client.demisto_api.models.incident_field import IncidentField
from demisto_client.demisto_api.models.incident_filter import IncidentFilter
from demisto_client.demisto_api.models.incident_search_response_wrapper import IncidentSearchResponseWrapper
from demisto_client.demisto_api.models.incident_status import IncidentStatus
from demisto_client.demisto_api.models.incident_type import IncidentType
from demisto_client.demisto_api.models.incident_wrapper import IncidentWrapper
from demisto_client.demisto_api.models.incidents import Incidents
from demisto_client.demisto_api.models.indicator_context import IndicatorContext
from demisto_client.demisto_api.models.indicator_edit_bulk_response import IndicatorEditBulkResponse
from demisto_client.demisto_api.models.indicator_filter import IndicatorFilter
from demisto_client.demisto_api.models.indicator_result import IndicatorResult
from demisto_client.demisto_api.models.inline_response200 import InlineResponse200
from demisto_client.demisto_api.models.insight_cache import InsightCache
from demisto_client.demisto_api.models.instance_classifier import InstanceClassifier
from demisto_client.demisto_api.models.integration_script import IntegrationScript
from demisto_client.demisto_api.models.inv_playbook_assignee import InvPlaybookAssignee
from demisto_client.demisto_api.models.inv_playbook_due import InvPlaybookDue
from demisto_client.demisto_api.models.inv_playbook_task_complete_data import InvPlaybookTaskCompleteData
from demisto_client.demisto_api.models.inv_playbook_task_data import InvPlaybookTaskData
from demisto_client.demisto_api.models.inv_task_info import InvTaskInfo
from demisto_client.demisto_api.models.investigation import Investigation
from demisto_client.demisto_api.models.investigation_filter import InvestigationFilter
from demisto_client.demisto_api.models.investigation_playbook import InvestigationPlaybook
from demisto_client.demisto_api.models.investigation_playbook_data import InvestigationPlaybookData
from demisto_client.demisto_api.models.investigation_playbook_state import InvestigationPlaybookState
from demisto_client.demisto_api.models.investigation_playbook_task import InvestigationPlaybookTask
from demisto_client.demisto_api.models.investigation_playbook_tasks_api import InvestigationPlaybookTasksAPI
from demisto_client.demisto_api.models.investigation_search_response import InvestigationSearchResponse
from demisto_client.demisto_api.models.investigation_status import InvestigationStatus
from demisto_client.demisto_api.models.investigation_type import InvestigationType
from demisto_client.demisto_api.models.investigations import Investigations
from demisto_client.demisto_api.models.ioc_object import IocObject
from demisto_client.demisto_api.models.ioc_objects import IocObjects
from demisto_client.demisto_api.models.label import Label
from demisto_client.demisto_api.models.layout import Layout
from demisto_client.demisto_api.models.layout_api import LayoutAPI
from demisto_client.demisto_api.models.layout_field import LayoutField
from demisto_client.demisto_api.models.layout_section import LayoutSection
from demisto_client.demisto_api.models.location import Location
from demisto_client.demisto_api.models.locations import Locations
from demisto_client.demisto_api.models.mapper import Mapper
from demisto_client.demisto_api.models.module_args import ModuleArgs
from demisto_client.demisto_api.models.module_configuration import ModuleConfiguration
from demisto_client.demisto_api.models.new_docker_image import NewDockerImage
from demisto_client.demisto_api.models.new_docker_image_result import NewDockerImageResult
from demisto_client.demisto_api.models.notifiable_item import NotifiableItem
from demisto_client.demisto_api.models.notify_timings import NotifyTimings
from demisto_client.demisto_api.models.operator_argument import OperatorArgument
from demisto_client.demisto_api.models.order import Order
from demisto_client.demisto_api.models.output import Output
from demisto_client.demisto_api.models.output_type import OutputType
from demisto_client.demisto_api.models.period import Period
from demisto_client.demisto_api.models.playbook import Playbook
from demisto_client.demisto_api.models.playbook_input import PlaybookInput
from demisto_client.demisto_api.models.playbook_inputs import PlaybookInputs
from demisto_client.demisto_api.models.playbook_output import PlaybookOutput
from demisto_client.demisto_api.models.playbook_outputs import PlaybookOutputs
from demisto_client.demisto_api.models.playbook_task import PlaybookTask
from demisto_client.demisto_api.models.playbook_view import PlaybookView
from demisto_client.demisto_api.models.question import Question
from demisto_client.demisto_api.models.quiet_mode import QuietMode
from demisto_client.demisto_api.models.raw_feed_indicator import RawFeedIndicator
from demisto_client.demisto_api.models.raw_message import RawMessage
from demisto_client.demisto_api.models.reliability import Reliability
from demisto_client.demisto_api.models.remote_repos import RemoteRepos
from demisto_client.demisto_api.models.report import Report
from demisto_client.demisto_api.models.report_automation import ReportAutomation
from demisto_client.demisto_api.models.report_fields_decoder import ReportFieldsDecoder
from demisto_client.demisto_api.models.report_query import ReportQuery
from demisto_client.demisto_api.models.reputation import Reputation
from demisto_client.demisto_api.models.reputation_calc_alg import ReputationCalcAlg
from demisto_client.demisto_api.models.reputation_data import ReputationData
from demisto_client.demisto_api.models.reputations_with_errors import ReputationsWithErrors
from demisto_client.demisto_api.models.run_status import RunStatus
from demisto_client.demisto_api.models.sla import SLA
from demisto_client.demisto_api.models.sla_state import SLAState
from demisto_client.demisto_api.models.script_api import ScriptAPI
from demisto_client.demisto_api.models.script_sub_type import ScriptSubType
from demisto_client.demisto_api.models.script_target import ScriptTarget
from demisto_client.demisto_api.models.script_type import ScriptType
from demisto_client.demisto_api.models.search_incidents_data import SearchIncidentsData
from demisto_client.demisto_api.models.section import Section
from demisto_client.demisto_api.models.section_item import SectionItem
from demisto_client.demisto_api.models.severity import Severity
from demisto_client.demisto_api.models.stats_query_response import StatsQueryResponse
from demisto_client.demisto_api.models.stats_text_response import StatsTextResponse
from demisto_client.demisto_api.models.stats_trends_response import StatsTrendsResponse
from demisto_client.demisto_api.models.system import System
from demisto_client.demisto_api.models.system_agent import SystemAgent
from demisto_client.demisto_api.models.task import Task
from demisto_client.demisto_api.models.task_condition import TaskCondition
from demisto_client.demisto_api.models.task_loop import TaskLoop
from demisto_client.demisto_api.models.task_state import TaskState
from demisto_client.demisto_api.models.task_type import TaskType
from demisto_client.demisto_api.models.task_view import TaskView
from demisto_client.demisto_api.models.term_location_map import TermLocationMap
from demisto_client.demisto_api.models.terminal_options import TerminalOptions
from demisto_client.demisto_api.models.timer_action import TimerAction
from demisto_client.demisto_api.models.timer_trigger import TimerTrigger
from demisto_client.demisto_api.models.transformer_operator_id import TransformerOperatorID
from demisto_client.demisto_api.models.update_data_batch import UpdateDataBatch
from demisto_client.demisto_api.models.update_entry import UpdateEntry
from demisto_client.demisto_api.models.update_entry_tags import UpdateEntryTags
from demisto_client.demisto_api.models.update_indicator_reputation_data import UpdateIndicatorReputationData
from demisto_client.demisto_api.models.update_response import UpdateResponse
from demisto_client.demisto_api.models.uploaded_entry import UploadedEntry
from demisto_client.demisto_api.models.version import Version
from demisto_client.demisto_api.models.widget import Widget
from demisto_client.demisto_api.models.widget_cell import WidgetCell
from demisto_client.demisto_api.models.widget_cells import WidgetCells
