# WebhookTestResponse

Result of POST .../test/ — same shape on success (200) and failure (400).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Delivery status of the test event (e.g. &#39;success&#39;, &#39;failed&#39;). | 
**message** | **str** | Human-readable description of the test outcome. | 
**delivery_uuid** | **UUID** | UUID of the delivery record created for this test. | 

## Example

```python
from financial_reports_generated_client.models.webhook_test_response import WebhookTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTestResponse from a JSON string
webhook_test_response_instance = WebhookTestResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookTestResponse.to_json())

# convert the object into a dict
webhook_test_response_dict = webhook_test_response_instance.to_dict()
# create an instance of WebhookTestResponse from a dict
webhook_test_response_from_dict = WebhookTestResponse.from_dict(webhook_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


