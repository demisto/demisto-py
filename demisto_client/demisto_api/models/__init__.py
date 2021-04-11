# coding: utf-8

# flake8: noqa
"""
    Cortex XSOAR API

    This is the public REST API to integrate with the Cortex XSOAR server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Cortex XSOAR web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Cortex XSOAR REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Cortex XSOAR server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Cortex XSOAR has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Cortex XSOAR will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

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
from demisto_client.demisto_api.models.authenticate_ok_body import AuthenticateOKBody
from demisto_client.demisto_api.models.automation_script import AutomationScript
from demisto_client.demisto_api.models.automation_script_filter import AutomationScriptFilter
from demisto_client.demisto_api.models.automation_script_filter_wrapper import AutomationScriptFilterWrapper
from demisto_client.demisto_api.models.automation_script_result import AutomationScriptResult
from demisto_client.demisto_api.models.base_filter import BaseFilter
from demisto_client.demisto_api.models.bucket import Bucket
from demisto_client.demisto_api.models.buckets import Buckets
from demisto_client.demisto_api.models.command import Command
from demisto_client.demisto_api.models.comment import Comment
from demisto_client.demisto_api.models.comment_type import CommentType
from demisto_client.demisto_api.models.comment_update import CommentUpdate
from demisto_client.demisto_api.models.comments import Comments
from demisto_client.demisto_api.models.comments_fields import CommentsFields
from demisto_client.demisto_api.models.common_fields import CommonFields
from demisto_client.demisto_api.models.common_update_batch import CommonUpdateBatch
from demisto_client.demisto_api.models.complex_arg import ComplexArg
from demisto_client.demisto_api.models.config_data_type import ConfigDataType
from demisto_client.demisto_api.models.config_field import ConfigField
from demisto_client.demisto_api.models.container_change_response_item import ContainerChangeResponseItem
from demisto_client.demisto_api.models.container_create_created_body import ContainerCreateCreatedBody
from demisto_client.demisto_api.models.container_top_ok_body import ContainerTopOKBody
from demisto_client.demisto_api.models.container_update_ok_body import ContainerUpdateOKBody
from demisto_client.demisto_api.models.container_wait_ok_body import ContainerWaitOKBody
from demisto_client.demisto_api.models.container_wait_ok_body_error import ContainerWaitOKBodyError
from demisto_client.demisto_api.models.containers_info import ContainersInfo
from demisto_client.demisto_api.models.content_item_exportable_fields import ContentItemExportableFields
from demisto_client.demisto_api.models.content_item_fields import ContentItemFields
from demisto_client.demisto_api.models.content_item_versioned_fields import ContentItemVersionedFields
from demisto_client.demisto_api.models.create_incident_request import CreateIncidentRequest
from demisto_client.demisto_api.models.custom_fields import CustomFields
from demisto_client.demisto_api.models.custom_group import CustomGroup
from demisto_client.demisto_api.models.custom_groups import CustomGroups
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
from demisto_client.demisto_api.models.elastic_common_fields import ElasticCommonFields
from demisto_client.demisto_api.models.elastic_version_fields import ElasticVersionFields
from demisto_client.demisto_api.models.ending_type import EndingType
from demisto_client.demisto_api.models.entry import Entry
from demisto_client.demisto_api.models.entry_category import EntryCategory
from demisto_client.demisto_api.models.entry_history import EntryHistory
from demisto_client.demisto_api.models.entry_reputation import EntryReputation
from demisto_client.demisto_api.models.entry_task import EntryTask
from demisto_client.demisto_api.models.entry_type import EntryType
from demisto_client.demisto_api.models.error_response import ErrorResponse
from demisto_client.demisto_api.models.evidence import Evidence
from demisto_client.demisto_api.models.evidence_data import EvidenceData
from demisto_client.demisto_api.models.evidences import Evidences
from demisto_client.demisto_api.models.evidences_filter_wrapper import EvidencesFilterWrapper
from demisto_client.demisto_api.models.evidences_search_response import EvidencesSearchResponse
from demisto_client.demisto_api.models.expiration_indicator import ExpirationIndicator
from demisto_client.demisto_api.models.expiration_policy import ExpirationPolicy
from demisto_client.demisto_api.models.expiration_settings_source import ExpirationSettingsSource
from demisto_client.demisto_api.models.expiration_source import ExpirationSource
from demisto_client.demisto_api.models.expiration_status import ExpirationStatus
from demisto_client.demisto_api.models.extract_settings_mode import ExtractSettingsMode
from demisto_client.demisto_api.models.feed_indicator import FeedIndicator
from demisto_client.demisto_api.models.feed_indicator_comment import FeedIndicatorComment
from demisto_client.demisto_api.models.feed_indicator_comments_fields import FeedIndicatorCommentsFields
from demisto_client.demisto_api.models.feed_indicators import FeedIndicators
from demisto_client.demisto_api.models.feed_indicators_request import FeedIndicatorsRequest
from demisto_client.demisto_api.models.feed_metadata import FeedMetadata
from demisto_client.demisto_api.models.field_extract_setting import FieldExtractSetting
from demisto_client.demisto_api.models.field_group import FieldGroup
from demisto_client.demisto_api.models.field_mapping import FieldMapping
from demisto_client.demisto_api.models.field_merge_strategy import FieldMergeStrategy
from demisto_client.demisto_api.models.field_term_location_map import FieldTermLocationMap
from demisto_client.demisto_api.models.file_metadata import FileMetadata
from demisto_client.demisto_api.models.filter_operator_id import FilterOperatorID
from demisto_client.demisto_api.models.form_display import FormDisplay
from demisto_client.demisto_api.models.full_version import FullVersion
from demisto_client.demisto_api.models.generic_indicator_update_batch import GenericIndicatorUpdateBatch
from demisto_client.demisto_api.models.generic_string_date_filter import GenericStringDateFilter
from demisto_client.demisto_api.models.generic_string_filter import GenericStringFilter
from demisto_client.demisto_api.models.graph_driver_data import GraphDriverData
from demisto_client.demisto_api.models.grid_column import GridColumn
from demisto_client.demisto_api.models.group import Group
from demisto_client.demisto_api.models.groups import Groups
from demisto_client.demisto_api.models.human_cron import HumanCron
from demisto_client.demisto_api.models.id_response import IdResponse
from demisto_client.demisto_api.models.id_version import IdVersion
from demisto_client.demisto_api.models.image_delete_response_item import ImageDeleteResponseItem
from demisto_client.demisto_api.models.image_summary import ImageSummary
from demisto_client.demisto_api.models.important import Important
from demisto_client.demisto_api.models.incident import Incident
from demisto_client.demisto_api.models.incident_field import IncidentField
from demisto_client.demisto_api.models.incident_fields_with_errors import IncidentFieldsWithErrors
from demisto_client.demisto_api.models.incident_filter import IncidentFilter
from demisto_client.demisto_api.models.incident_search_response_wrapper import IncidentSearchResponseWrapper
from demisto_client.demisto_api.models.incident_status import IncidentStatus
from demisto_client.demisto_api.models.incident_type import IncidentType
from demisto_client.demisto_api.models.incident_type_extract_settings import IncidentTypeExtractSettings
from demisto_client.demisto_api.models.incident_types_with_errors import IncidentTypesWithErrors
from demisto_client.demisto_api.models.incident_wrapper import IncidentWrapper
from demisto_client.demisto_api.models.incidents import Incidents
from demisto_client.demisto_api.models.indicator_context import IndicatorContext
from demisto_client.demisto_api.models.indicator_edit_bulk_response import IndicatorEditBulkResponse
from demisto_client.demisto_api.models.indicator_filter import IndicatorFilter
from demisto_client.demisto_api.models.indicator_result import IndicatorResult
from demisto_client.demisto_api.models.indicator_timeline import IndicatorTimeline
from demisto_client.demisto_api.models.indicator_timeline_from_entry import IndicatorTimelineFromEntry
from demisto_client.demisto_api.models.info import Info
from demisto_client.demisto_api.models.inline_response200 import InlineResponse200
from demisto_client.demisto_api.models.insight_cache import InsightCache
from demisto_client.demisto_api.models.instance_classifier import InstanceClassifier
from demisto_client.demisto_api.models.integration_script import IntegrationScript
from demisto_client.demisto_api.models.inv_playbook_assignee import InvPlaybookAssignee
from demisto_client.demisto_api.models.inv_playbook_debug_info import InvPlaybookDebugInfo
from demisto_client.demisto_api.models.inv_playbook_due import InvPlaybookDue
from demisto_client.demisto_api.models.inv_playbook_task_complete_data import InvPlaybookTaskCompleteData
from demisto_client.demisto_api.models.inv_playbook_task_data import InvPlaybookTaskData
from demisto_client.demisto_api.models.inv_task_debug import InvTaskDebug
from demisto_client.demisto_api.models.inv_task_info import InvTaskInfo
from demisto_client.demisto_api.models.investigation import Investigation
from demisto_client.demisto_api.models.investigation_filter import InvestigationFilter
from demisto_client.demisto_api.models.investigation_playbook import InvestigationPlaybook
from demisto_client.demisto_api.models.investigation_playbook_data import InvestigationPlaybookData
from demisto_client.demisto_api.models.investigation_playbook_state import InvestigationPlaybookState
from demisto_client.demisto_api.models.investigation_playbook_task import InvestigationPlaybookTask
from demisto_client.demisto_api.models.investigation_search_response import InvestigationSearchResponse
from demisto_client.demisto_api.models.investigation_status import InvestigationStatus
from demisto_client.demisto_api.models.investigation_type import InvestigationType
from demisto_client.demisto_api.models.investigations import Investigations
from demisto_client.demisto_api.models.ioc_object import IocObject
from demisto_client.demisto_api.models.ioc_objects import IocObjects
from demisto_client.demisto_api.models.label import Label
from demisto_client.demisto_api.models.layout import Layout
from demisto_client.demisto_api.models.layout_api import LayoutAPI
from demisto_client.demisto_api.models.layout_common import LayoutCommon
from demisto_client.demisto_api.models.layout_field import LayoutField
from demisto_client.demisto_api.models.layout_section import LayoutSection
from demisto_client.demisto_api.models.location import Location
from demisto_client.demisto_api.models.locations import Locations
from demisto_client.demisto_api.models.mapper import Mapper
from demisto_client.demisto_api.models.mapper_type import MapperType
from demisto_client.demisto_api.models.module_args import ModuleArgs
from demisto_client.demisto_api.models.module_configuration import ModuleConfiguration
from demisto_client.demisto_api.models.new_docker_image import NewDockerImage
from demisto_client.demisto_api.models.new_docker_image_result import NewDockerImageResult
from demisto_client.demisto_api.models.notifiable_item import NotifiableItem
from demisto_client.demisto_api.models.notify_timings import NotifyTimings
from demisto_client.demisto_api.models.operator_argument import OperatorArgument
from demisto_client.demisto_api.models.operator_type import OperatorType
from demisto_client.demisto_api.models.order import Order
from demisto_client.demisto_api.models.output import Output
from demisto_client.demisto_api.models.output_type import OutputType
from demisto_client.demisto_api.models.period import Period
from demisto_client.demisto_api.models.playbook import Playbook
from demisto_client.demisto_api.models.playbook_input import PlaybookInput
from demisto_client.demisto_api.models.playbook_input_query import PlaybookInputQuery
from demisto_client.demisto_api.models.playbook_inputs import PlaybookInputs
from demisto_client.demisto_api.models.playbook_output import PlaybookOutput
from demisto_client.demisto_api.models.playbook_outputs import PlaybookOutputs
from demisto_client.demisto_api.models.playbook_task import PlaybookTask
from demisto_client.demisto_api.models.playbook_view import PlaybookView
from demisto_client.demisto_api.models.playbook_with_warnings import PlaybookWithWarnings
from demisto_client.demisto_api.models.plugin import Plugin
from demisto_client.demisto_api.models.plugin_config import PluginConfig
from demisto_client.demisto_api.models.plugin_config_args import PluginConfigArgs
from demisto_client.demisto_api.models.plugin_config_interface import PluginConfigInterface
from demisto_client.demisto_api.models.plugin_config_linux import PluginConfigLinux
from demisto_client.demisto_api.models.plugin_config_network import PluginConfigNetwork
from demisto_client.demisto_api.models.plugin_config_rootfs import PluginConfigRootfs
from demisto_client.demisto_api.models.plugin_config_user import PluginConfigUser
from demisto_client.demisto_api.models.plugin_device import PluginDevice
from demisto_client.demisto_api.models.plugin_env import PluginEnv
from demisto_client.demisto_api.models.plugin_interface_type import PluginInterfaceType
from demisto_client.demisto_api.models.plugin_mount import PluginMount
from demisto_client.demisto_api.models.plugin_settings import PluginSettings
from demisto_client.demisto_api.models.port import Port
from demisto_client.demisto_api.models.process_info import ProcessInfo
from demisto_client.demisto_api.models.query_state import QueryState
from demisto_client.demisto_api.models.question import Question
from demisto_client.demisto_api.models.quiet_mode import QuietMode
from demisto_client.demisto_api.models.rbac import RBAC
from demisto_client.demisto_api.models.raw_feed_indicator import RawFeedIndicator
from demisto_client.demisto_api.models.relationship_api import RelationshipAPI
from demisto_client.demisto_api.models.relationship_common_fields import RelationshipCommonFields
from demisto_client.demisto_api.models.relationship_filter import RelationshipFilter
from demisto_client.demisto_api.models.relationships_api import RelationshipsAPI
from demisto_client.demisto_api.models.reliability import Reliability
from demisto_client.demisto_api.models.report import Report
from demisto_client.demisto_api.models.report_automation import ReportAutomation
from demisto_client.demisto_api.models.report_fields_decoder import ReportFieldsDecoder
from demisto_client.demisto_api.models.report_query import ReportQuery
from demisto_client.demisto_api.models.reputation_calc_alg import ReputationCalcAlg
from demisto_client.demisto_api.models.reputation_data import ReputationData
from demisto_client.demisto_api.models.run_status import RunStatus
from demisto_client.demisto_api.models.sla import SLA
from demisto_client.demisto_api.models.sla_state import SLAState
from demisto_client.demisto_api.models.schedule import Schedule
from demisto_client.demisto_api.models.scheduler import Scheduler
from demisto_client.demisto_api.models.script_api import ScriptAPI
from demisto_client.demisto_api.models.script_sub_type import ScriptSubType
from demisto_client.demisto_api.models.script_target import ScriptTarget
from demisto_client.demisto_api.models.script_type import ScriptType
from demisto_client.demisto_api.models.search_incidents_data import SearchIncidentsData
from demisto_client.demisto_api.models.search_investigations_data import SearchInvestigationsData
from demisto_client.demisto_api.models.search_stats import SearchStats
from demisto_client.demisto_api.models.search_stats_deletion_response import SearchStatsDeletionResponse
from demisto_client.demisto_api.models.search_stats_response import SearchStatsResponse
from demisto_client.demisto_api.models.section import Section
from demisto_client.demisto_api.models.service_update_response import ServiceUpdateResponse
from demisto_client.demisto_api.models.severity import Severity
from demisto_client.demisto_api.models.sharded_fields import ShardedFields
from demisto_client.demisto_api.models.stats_query_error import StatsQueryError
from demisto_client.demisto_api.models.stats_query_response import StatsQueryResponse
from demisto_client.demisto_api.models.stats_query_response_with_error import StatsQueryResponseWithError
from demisto_client.demisto_api.models.stats_response_with_reference_line import StatsResponseWithReferenceLine
from demisto_client.demisto_api.models.stats_scatter_response import StatsScatterResponse
from demisto_client.demisto_api.models.stats_text_response import StatsTextResponse
from demisto_client.demisto_api.models.stats_trends_response import StatsTrendsResponse
from demisto_client.demisto_api.models.system import System
from demisto_client.demisto_api.models.system_agent import SystemAgent
from demisto_client.demisto_api.models.tags_field_values import TagsFieldValues
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
from demisto_client.demisto_api.models.type_and_kind import TypeAndKind
from demisto_client.demisto_api.models.unclassified_cases import UnclassifiedCases
from demisto_client.demisto_api.models.update_data_batch import UpdateDataBatch
from demisto_client.demisto_api.models.update_entry import UpdateEntry
from demisto_client.demisto_api.models.update_entry_tags import UpdateEntryTags
from demisto_client.demisto_api.models.update_indicator_batch import UpdateIndicatorBatch
from demisto_client.demisto_api.models.update_indicator_reputation_data import UpdateIndicatorReputationData
from demisto_client.demisto_api.models.update_response import UpdateResponse
from demisto_client.demisto_api.models.uploaded_entry import UploadedEntry
from demisto_client.demisto_api.models.version import Version
from demisto_client.demisto_api.models.versioned_commit import VersionedCommit
from demisto_client.demisto_api.models.volume import Volume
from demisto_client.demisto_api.models.volume_usage_data import VolumeUsageData
from demisto_client.demisto_api.models.whitelisted_indicator import WhitelistedIndicator
from demisto_client.demisto_api.models.widget import Widget
from demisto_client.demisto_api.models.widget_cell import WidgetCell
from demisto_client.demisto_api.models.widget_cells import WidgetCells
from demisto_client.demisto_api.models.with_custom_fields import WithCustomFields
