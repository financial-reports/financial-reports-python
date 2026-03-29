# WebhookDeliveryDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**webhook_id** | **int** |  | [readonly] 
**event_type** | **str** |  | [readonly] 
**filing_id** | **int** | ID of the filing reference to reconstruct payload | [readonly] 
**status** | [**StatusEnum**](StatusEnum.md) |  | [readonly] 
**response_status_code** | **int** |  | [readonly] 
**duration_ms** | **int** |  | [readonly] 
**response_body** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**request_headers** | **Dict[str, object]** | Reconstructed request headers that were sent with this delivery. | [readonly] 
**request_payload** | **Dict[str, object]** | Reconstructed request payload. Built dynamically from the referenced filing. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.webhook_delivery_detail import WebhookDeliveryDetail

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryDetail from a JSON string
webhook_delivery_detail_instance = WebhookDeliveryDetail.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryDetail.to_json())

# convert the object into a dict
webhook_delivery_detail_dict = webhook_delivery_detail_instance.to_dict()
# create an instance of WebhookDeliveryDetail from a dict
webhook_delivery_detail_from_dict = WebhookDeliveryDetail.from_dict(webhook_delivery_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


