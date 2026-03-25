# ChatSessionUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from financial_reports_generated_client.models.chat_session_update_response import ChatSessionUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatSessionUpdateResponse from a JSON string
chat_session_update_response_instance = ChatSessionUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(ChatSessionUpdateResponse.to_json())

# convert the object into a dict
chat_session_update_response_dict = chat_session_update_response_instance.to_dict()
# create an instance of ChatSessionUpdateResponse from a dict
chat_session_update_response_from_dict = ChatSessionUpdateResponse.from_dict(chat_session_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


