# DividendUpdatedPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | &#39;dividend.created&#39; or &#39;dividend.updated&#39;. | [readonly] 
**webhook_id** | **str** | The ID of the webhook configuration that triggered this event. | [readonly] 
**company_id** | **str** | The company that declared the dividend. | [readonly] 
**dividend_id** | **str** | The dividend&#39;s stable id (&#x60;dividend.id&#x60;). | [readonly] 
**dividend** | **object** | The dividend as it is now: one item of GET /companies/{id}/dividends/, same fields. | [readonly] 
**triggered_at** | **datetime** | The timestamp (ISO 8601) when the event was triggered. | [readonly] 
**changes** | **object** | What this notice changed: a list of {&#39;field&#39;, &#39;old&#39;, &#39;new&#39;, &#39;filing_id&#39;}. &#39;field&#39; is a date (&#39;ex_date&#39;, &#39;record_date&#39;, &#39;payment_date&#39;, &#39;last_cum_date&#39;, &#39;agm_date&#39;; &#39;old&#39; is null when it was not known), &#39;stage&#39; (&#39;proposed&#39; to &#39;declared&#39;) or &#39;is_cancelled&#39;. &#39;filing_id&#39; is the notice, null when your plan does not list it. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.dividend_updated_payload import DividendUpdatedPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DividendUpdatedPayload from a JSON string
dividend_updated_payload_instance = DividendUpdatedPayload.from_json(json)
# print the JSON string representation of the object
print(DividendUpdatedPayload.to_json())

# convert the object into a dict
dividend_updated_payload_dict = dividend_updated_payload_instance.to_dict()
# create an instance of DividendUpdatedPayload from a dict
dividend_updated_payload_from_dict = DividendUpdatedPayload.from_dict(dividend_updated_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


