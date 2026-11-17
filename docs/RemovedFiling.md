# RemovedFiling

One filing you could see that is no longer available to you (#10443).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filing_id** | **int** | Id of the filing. Delete it from your copy; &#x60;GET /filings/{id}/&#x60; now returns 404. | [readonly] 
**reason** | [**RemovedFilingReasonEnum**](RemovedFilingReasonEnum.md) | &#x60;hidden&#x60;: withdrawn. &#x60;duplicate_copy&#x60;: a byte-identical copy of another filing, which stays available under its own id. &#x60;company_hidden&#x60;: re-attributed to a company we do not list. &#x60;out_of_scope&#x60;: re-attributed to a company outside your plan.  * &#x60;hidden&#x60; - The filing was withdrawn from the platform. * &#x60;duplicate_copy&#x60; - The filing is a copy of another filing, which stays. * &#x60;company_hidden&#x60; - The filing was moved onto a company that is not listed. * &#x60;out_of_scope&#x60; - The filing was moved to a company outside your plan. | [readonly] 
**removed_at** | **datetime** | When the change was recorded (ISO 8601, UTC). For &#x60;hidden&#x60; and &#x60;duplicate_copy&#x60; it is the filing&#39;s last change, so a later change lists the filing again. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.removed_filing import RemovedFiling

# TODO update the JSON string below
json = "{}"
# create an instance of RemovedFiling from a JSON string
removed_filing_instance = RemovedFiling.from_json(json)
# print the JSON string representation of the object
print(RemovedFiling.to_json())

# convert the object into a dict
removed_filing_dict = removed_filing_instance.to_dict()
# create an instance of RemovedFiling from a dict
removed_filing_from_dict = RemovedFiling.from_dict(removed_filing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


