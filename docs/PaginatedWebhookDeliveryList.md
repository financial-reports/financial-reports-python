# PaginatedWebhookDeliveryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total matching results. Exact for cheap queries, an estimate on broad or expensive ones. Do not use it to decide when to stop: follow &#x60;next&#x60; until it is null. | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[WebhookDelivery]**](WebhookDelivery.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_webhook_delivery_list import PaginatedWebhookDeliveryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWebhookDeliveryList from a JSON string
paginated_webhook_delivery_list_instance = PaginatedWebhookDeliveryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedWebhookDeliveryList.to_json())

# convert the object into a dict
paginated_webhook_delivery_list_dict = paginated_webhook_delivery_list_instance.to_dict()
# create an instance of PaginatedWebhookDeliveryList from a dict
paginated_webhook_delivery_list_from_dict = PaginatedWebhookDeliveryList.from_dict(paginated_webhook_delivery_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


