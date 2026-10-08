# FilingUpdatedPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The name of the event (e.g., &#39;filing.processed&#39; or &#39;filing.received&#39;). | [readonly] 
**webhook_id** | **str** | The ID of the webhook configuration that triggered this event. | [readonly] 
**filing_id** | **str** | The ID of the newly processed filing. | [readonly] 
**company** | [**WebhookCompanyPayload**](WebhookCompanyPayload.md) | Details of the company associated with the filing. | [readonly] 
**filing** | [**WebhookFilingPayload**](WebhookFilingPayload.md) | Details of the filing itself. | [readonly] 
**triggered_at** | **datetime** | The timestamp (ISO 8601) when the event was triggered. | [readonly] 
**changes** | **object** | What changed since the last version you received, keyed by field: &#39;filing_type&#39; ({&#39;from&#39;: code, &#39;to&#39;: code}) and/or &#39;company&#39; ({&#39;from&#39;: company id, &#39;to&#39;: company id}). Empty when a filing you were told was removed is visible again, and on a replay. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.filing_updated_payload import FilingUpdatedPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FilingUpdatedPayload from a JSON string
filing_updated_payload_instance = FilingUpdatedPayload.from_json(json)
# print the JSON string representation of the object
print(FilingUpdatedPayload.to_json())

# convert the object into a dict
filing_updated_payload_dict = filing_updated_payload_instance.to_dict()
# create an instance of FilingUpdatedPayload from a dict
filing_updated_payload_from_dict = FilingUpdatedPayload.from_dict(filing_updated_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


