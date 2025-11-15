# WebhookFilingPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal Financial Reports Filing ID. | [readonly] 
**filing_type_code** | **str** | Short code for the filing type (e.g., &#39;10-K&#39;). | [readonly] 
**filing_type_name** | **str** | Human-readable filing type (e.g., &#39;Annual Report&#39;). | [readonly] 
**language_code** | **str** | ISO 639-1 language code (e.g., &#39;en&#39;). | [readonly] 
**language_name** | **str** | Human-readable language name (e.g., &#39;English&#39;). | [readonly] 
**title** | **str** | The title of the filing. | [readonly] 
**dissemination_datetime** | **datetime** | The exact time the filing was disseminated by the source. | [readonly] 
**release_datetime** | **datetime** | The official release time of the filing (e.S., the period end). | [readonly] 
**document_url** | **str** | A direct, temporary link to download the original filing document (e.g., PDF). | [readonly] 
**markdown_content** | **str** | The full, processed content of the filing in Markdown format. This field is only included if your webhook is configured with &#39;include_markdown: true&#39;. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.webhook_filing_payload import WebhookFilingPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookFilingPayload from a JSON string
webhook_filing_payload_instance = WebhookFilingPayload.from_json(json)
# print the JSON string representation of the object
print(WebhookFilingPayload.to_json())

# convert the object into a dict
webhook_filing_payload_dict = webhook_filing_payload_instance.to_dict()
# create an instance of WebhookFilingPayload from a dict
webhook_filing_payload_from_dict = WebhookFilingPayload.from_dict(webhook_filing_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


