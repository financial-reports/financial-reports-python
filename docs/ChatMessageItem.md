# ChatMessageItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**role** | **str** |  | 
**content** | **str** |  | 
**thought_signature** | **str** |  | 
**tool_calls** | [**OneOf**](OneOf.md) |  | 
**tool_results** | [**OneOf**](OneOf.md) |  | 
**created_at** | **datetime** |  | 

## Example

```python
from financial_reports_generated_client.models.chat_message_item import ChatMessageItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessageItem from a JSON string
chat_message_item_instance = ChatMessageItem.from_json(json)
# print the JSON string representation of the object
print(ChatMessageItem.to_json())

# convert the object into a dict
chat_message_item_dict = chat_message_item_instance.to_dict()
# create an instance of ChatMessageItem from a dict
chat_message_item_from_dict = ChatMessageItem.from_dict(chat_message_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


