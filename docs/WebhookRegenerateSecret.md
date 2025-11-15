# WebhookRegenerateSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_key** | **str** | The newly generated secret key. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.webhook_regenerate_secret import WebhookRegenerateSecret

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegenerateSecret from a JSON string
webhook_regenerate_secret_instance = WebhookRegenerateSecret.from_json(json)
# print the JSON string representation of the object
print(WebhookRegenerateSecret.to_json())

# convert the object into a dict
webhook_regenerate_secret_dict = webhook_regenerate_secret_instance.to_dict()
# create an instance of WebhookRegenerateSecret from a dict
webhook_regenerate_secret_from_dict = WebhookRegenerateSecret.from_dict(webhook_regenerate_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


