# WebhookSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_key** | **str** | The unique secret key for the webhook. This is shown only once. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.webhook_secret import WebhookSecret

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecret from a JSON string
webhook_secret_instance = WebhookSecret.from_json(json)
# print the JSON string representation of the object
print(WebhookSecret.to_json())

# convert the object into a dict
webhook_secret_dict = webhook_secret_instance.to_dict()
# create an instance of WebhookSecret from a dict
webhook_secret_from_dict = WebhookSecret.from_dict(webhook_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


