# WebhookReplayResponse

Result of POST .../deliveries/{uuid}/replay/.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Indicates the replay was accepted (e.g. &#39;success&#39;). | 
**message** | **str** | Human-readable description of the replay outcome. | 

## Example

```python
from financial_reports_generated_client.models.webhook_replay_response import WebhookReplayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookReplayResponse from a JSON string
webhook_replay_response_instance = WebhookReplayResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookReplayResponse.to_json())

# convert the object into a dict
webhook_replay_response_dict = webhook_replay_response_instance.to_dict()
# create an instance of WebhookReplayResponse from a dict
webhook_replay_response_from_dict = WebhookReplayResponse.from_dict(webhook_replay_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


