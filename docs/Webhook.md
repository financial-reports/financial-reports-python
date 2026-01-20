# Webhook

Serializer for the Webhook model. Handles create, retrieve, update, and list operations for a user's webhooks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the webhook. | [readonly] 
**url** | **str** | The endpoint URL (HTTPS required) to which the webhook payloads will be sent. | 
**is_active** | **bool** | Set to &#39;false&#39; to temporarily disable this webhook without deleting it. | [optional] [default to True]
**include_markdown** | **bool** | Set to &#39;true&#39; to include the full &#39;markdown_content&#39; in the webhook payload. Set to &#39;false&#39; to receive a payload without the markdown body. | [optional] [default to True]
**include_isins** | **bool** | Set to &#39;true&#39; to include the list of ISINs in the company object. Warning: Large companies may have thousands of ISINs, increasing payload size. | [optional] [default to False]
**track_all_companies** | **bool** | Set to &#39;true&#39; to subscribe to the Global Firehose. You will receive notifications for filings from ALL companies in the database, regardless of your Watchlist. | [optional] [default to False]
**subscribed_filing_types** | **List[str]** | A list of filing type codes (e.g., [&#39;10-K&#39;, &#39;Annual Report&#39;]) to subscribe to. If this list is empty or omitted, you will be subscribed to all filing types. | [optional] 
**secret_key** | **str** | Your unique secret key for verifying payload signatures. This key is generated upon creation and can be regenerated via a separate endpoint. | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


