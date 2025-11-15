# PaginatedWebhookList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Webhook]**](Webhook.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_webhook_list import PaginatedWebhookList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWebhookList from a JSON string
paginated_webhook_list_instance = PaginatedWebhookList.from_json(json)
# print the JSON string representation of the object
print(PaginatedWebhookList.to_json())

# convert the object into a dict
paginated_webhook_list_dict = paginated_webhook_list_instance.to_dict()
# create an instance of PaginatedWebhookList from a dict
paginated_webhook_list_from_dict = PaginatedWebhookList.from_dict(paginated_webhook_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


