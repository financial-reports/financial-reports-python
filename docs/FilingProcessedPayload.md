# FilingProcessedPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The name of the event (e.g., &#39;filing.processed&#39;). | [readonly] 
**webhook_id** | **str** | The ID of the webhook configuration that triggered this event. | [readonly] 
**filing_id** | **str** | The ID of the newly processed filing. | [readonly] 
**company** | [**WebhookCompanyPayload**](WebhookCompanyPayload.md) | Details of the company associated with the filing. | [readonly] 
**filing** | [**WebhookFilingPayload**](WebhookFilingPayload.md) | Details of the filing itself. | [readonly] 
**triggered_at** | **datetime** | The timestamp (ISO 8601) when the event was triggered. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.filing_processed_payload import FilingProcessedPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FilingProcessedPayload from a JSON string
filing_processed_payload_instance = FilingProcessedPayload.from_json(json)
# print the JSON string representation of the object
print(FilingProcessedPayload.to_json())

# convert the object into a dict
filing_processed_payload_dict = filing_processed_payload_instance.to_dict()
# create an instance of FilingProcessedPayload from a dict
filing_processed_payload_from_dict = FilingProcessedPayload.from_dict(filing_processed_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


