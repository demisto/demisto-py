# DBotScore
DBot is the Demisto machine learning bot which ingests information about indicators to determine if they are malicious or not.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**content_format** | **str** |  | [optional] 
**context** | **dict(str, object)** |  | [optional] 
**is_typed_indicator** | **bool** | Indicates if indicator has a type assigned to it. | [optional] 
**score** | **int** | Dbot uses an integer to represent the reputation of an indicator. 0 - Unknown, 1 - Good, 2 - Suspicious, 3 - Malicious | [optional] 
**score_change_timestamp** | **datetime** | We need to track when the score changes to know if we need to re-calculate the overall score | [optional] 
**timestamp** | **datetime** | Datetime object of time DBot Score is reported. | [optional] 
**type** | **str** | Type of Indicator. Can be: `ip`, `file`, `email`, or `url` | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


