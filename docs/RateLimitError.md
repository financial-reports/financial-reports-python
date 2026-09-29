# RateLimitError

Body of a 429 response. The `Retry-After` header carries the same wait as `retry_after_seconds`. Only `detail` is always present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | A human-readable message describing the error. | 
**error** | **str** | Always &#x60;Too Many Requests&#x60;. | [optional] 
**retry_after_seconds** | **int** | Seconds until the request may be retried, when known. | [optional] 
**scope** | **str** | Which limit was hit, e.g. &#x60;burst&#x60;, &#x60;quota&#x60; or &#x60;payg_velocity&#x60;. | [optional] 
**type** | **str** | Machine-readable error code, e.g. &#x60;burst_limit_exceeded&#x60;, &#x60;quota_limit_exceeded&#x60;, &#x60;daily_spend_cap_reached&#x60; or &#x60;monthly_spend_ceiling_reached&#x60;. | [optional] 
**message** | **str** | A human-readable explanation of the limit. | [optional] 
**resolution** | **str** | A human-readable hint on what to do next. | [optional] 
**upgrade_url** | **str** | Where to upgrade the plan (quota errors). | [optional] 
**limit** | **int** | The plan allowance that was used up (quota errors). | [optional] 
**interval** | **str** | &#x60;monthly&#x60; or &#x60;annual&#x60; (quota errors). | [optional] 
**payg_url** | **str** | Where to enable pay-as-you-go (some quota errors). | [optional] 
**contact** | **str** | Who to contact to raise the limit (spend-ceiling errors). | [optional] 

## Example

```python
from financial_reports_generated_client.models.rate_limit_error import RateLimitError

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitError from a JSON string
rate_limit_error_instance = RateLimitError.from_json(json)
# print the JSON string representation of the object
print(RateLimitError.to_json())

# convert the object into a dict
rate_limit_error_dict = rate_limit_error_instance.to_dict()
# create an instance of RateLimitError from a dict
rate_limit_error_from_dict = RateLimitError.from_dict(rate_limit_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


