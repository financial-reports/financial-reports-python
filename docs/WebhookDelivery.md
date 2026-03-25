# WebhookDelivery

Serializer for the WebhookDelivery model (Delivery Logs). Allows users to audit the history of events sent to their endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**webhook_id** | **int** |  | [readonly] 
**event_type** | **str** |  | [readonly] 
**status** | [**StatusEnum**](StatusEnum.md) |  | [readonly] 
**response_status_code** | **int** |  | [readonly] 
**duration_ms** | **int** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**request_headers** | **object** |  | [readonly] 
**request_payload** | **object** |  | [readonly] 
**response_body** | **str** |  | [readonly] 
**response_headers** | **object** |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.webhook_delivery import WebhookDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDelivery from a JSON string
webhook_delivery_instance = WebhookDelivery.from_json(json)
# print the JSON string representation of the object
print(WebhookDelivery.to_json())

# convert the object into a dict
webhook_delivery_dict = webhook_delivery_instance.to_dict()
# create an instance of WebhookDelivery from a dict
webhook_delivery_from_dict = WebhookDelivery.from_dict(webhook_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


