# ChatInteractionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** | The user&#39;s message or question for the financial agent. | [optional] 
**session_id** | **int** | ID of an existing chat session to resume. If omitted, a new session is created. | [optional] 
**company_id** | **int** | Optional: Restrict the agent&#39;s context strictly to this specific company. | [optional] 
**filing_ids** | **List[int]** | Optional: Restrict the agent&#39;s context to specific filings (triggers direct File Search RAG). | [optional] 
**title** | **str** | Title for the chat if a new session is being created. | [optional] [default to 'New Chat']

## Example

```python
from financial_reports_generated_client.models.chat_interaction_request import ChatInteractionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChatInteractionRequest from a JSON string
chat_interaction_request_instance = ChatInteractionRequest.from_json(json)
# print the JSON string representation of the object
print(ChatInteractionRequest.to_json())

# convert the object into a dict
chat_interaction_request_dict = chat_interaction_request_instance.to_dict()
# create an instance of ChatInteractionRequest from a dict
chat_interaction_request_from_dict = ChatInteractionRequest.from_dict(chat_interaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


