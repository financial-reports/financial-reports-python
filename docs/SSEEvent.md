# SSEEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**args** | **object** |  | [optional] 
**result** | **object** |  | [optional] 
**status** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.sse_event import SSEEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SSEEvent from a JSON string
sse_event_instance = SSEEvent.from_json(json)
# print the JSON string representation of the object
print(SSEEvent.to_json())

# convert the object into a dict
sse_event_dict = sse_event_instance.to_dict()
# create an instance of SSEEvent from a dict
sse_event_from_dict = SSEEvent.from_dict(sse_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


