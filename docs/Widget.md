# Widget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category the widget is related to. Used to display in widget library under category or dataType if empty. | [optional] 
**commit_message** | **str** |  | [optional] 
**data_type** | **str** | Data type of the widget. Describes what data does the widget query. supporting data types \&quot;incidents\&quot;,\&quot;messages\&quot;,\&quot;system\&quot;,\&quot;entries\&quot;,\&quot;tasks\&quot;, \&quot;audit\&quot;. | [optional] 
**date_range** | [**DateRange**](DateRange.md) |  | [optional] 
**description** | **str** | The description of the widget&#39;s usage and data representation. | [optional] 
**id** | **str** |  | [optional] 
**is_predefined** | **bool** | Is the widget a system widget. | [optional] 
**locked** | **bool** | Is the widget locked for editing. | [optional] 
**modified** | **datetime** |  | [optional] 
**name** | **str** | Default name of the widget. | 
**params** | **dict(str, object)** | Additional parameters for this widget, depends on widget type and data. | [optional] 
**prev_name** | **str** | The previous name of the widget. | [optional] 
**query** | **str** | Query to search on the dataType. | [optional] 
**should_commit** | **bool** |  | [optional] 
**size** | **int** | Maximum size for this widget data returned. | [optional] 
**sort** | [**list[Order]**](Order.md) | Sorting array to sort the data received by the given Order parameters. | [optional] 
**sort_values** | **list[str]** |  | [optional] 
**vc_should_ignore** | **bool** |  | [optional] 
**version** | **int** |  | [optional] 
**widget_type** | **str** | Widget type describes how does the widget should recieve the data, and display it. Supporting types: \&quot;bar\&quot;, \&quot;column\&quot;, \&quot;pie\&quot;, \&quot;list\&quot;, \&quot;number\&quot;, \&quot;trend\&quot;, \&quot;text\&quot;, \&quot;duration\&quot;, \&quot;image\&quot;, \&quot;line\&quot;, and \&quot;table\&quot;. | 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


