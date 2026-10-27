# DividendEventPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | &#39;dividend.created&#39; or &#39;dividend.updated&#39;. | [readonly] 
**webhook_id** | **str** | The ID of the webhook configuration that triggered this event. | [readonly] 
**company_id** | **str** | The company that declared the dividend. | [readonly] 
**dividend_id** | **str** | The dividend&#39;s stable id (&#x60;dividend.id&#x60;). | [readonly] 
**dividend** | **object** | The dividend as it is now: one item of GET /companies/{id}/dividends/, same fields. | [readonly] 
**triggered_at** | **datetime** | The timestamp (ISO 8601) when the event was triggered. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.dividend_event_payload import DividendEventPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DividendEventPayload from a JSON string
dividend_event_payload_instance = DividendEventPayload.from_json(json)
# print the JSON string representation of the object
print(DividendEventPayload.to_json())

# convert the object into a dict
dividend_event_payload_dict = dividend_event_payload_instance.to_dict()
# create an instance of DividendEventPayload from a dict
dividend_event_payload_from_dict = DividendEventPayload.from_dict(dividend_event_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


