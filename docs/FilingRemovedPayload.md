# FilingRemovedPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | Always &#39;filing.removed&#39;. | [readonly] 
**webhook_id** | **str** | The ID of the webhook configuration that triggered this event. | [readonly] 
**filing_id** | **str** | The ID of the filing you should discard. | [readonly] 
**reason** | **str** | &#39;deleted&#39;: the filing no longer exists. &#39;hidden&#39;: it was withdrawn from the platform. &#39;company_hidden&#39;: its company was withdrawn. &#39;out_of_scope&#39;: it was re-typed or moved to a company outside this webhook&#39;s filing types, watchlist or plan.  * &#x60;deleted&#x60; - deleted * &#x60;hidden&#x60; - hidden * &#x60;company_hidden&#x60; - company_hidden * &#x60;out_of_scope&#x60; - out_of_scope | [readonly] 
**triggered_at** | **datetime** | The timestamp (ISO 8601) when the event was triggered. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.filing_removed_payload import FilingRemovedPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FilingRemovedPayload from a JSON string
filing_removed_payload_instance = FilingRemovedPayload.from_json(json)
# print the JSON string representation of the object
print(FilingRemovedPayload.to_json())

# convert the object into a dict
filing_removed_payload_dict = filing_removed_payload_instance.to_dict()
# create an instance of FilingRemovedPayload from a dict
filing_removed_payload_from_dict = FilingRemovedPayload.from_dict(filing_removed_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


