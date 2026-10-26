# CompaniesSegmentsRetrieve200ResponseSegmentsInnerValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | 
**period** | **str** | &#x60;FY&#x60;, &#x60;9M&#x60;, &#x60;H&#x60; or &#x60;Q&#x60; by the period&#39;s length; &#x60;null&#x60; for a balance (assets) or an unusual length. | 
**period_start** | **date** |  | 
**period_end** | **date** |  | 
**value** | **decimal.Decimal** |  | 
**currency** | **str** |  | 
**concept** | **str** | The XBRL concept the filer tagged the figure with. | 
**member** | **str** | The XBRL axis member the filer tagged the figure with. | 
**source_filing** | [**CompaniesSegmentsRetrieve200ResponseSegmentsInnerValuesInnerSourceFiling**](CompaniesSegmentsRetrieve200ResponseSegmentsInnerValuesInnerSourceFiling.md) |  | 

## Example

```python
from financial_reports_generated_client.models.companies_segments_retrieve200_response_segments_inner_values_inner import CompaniesSegmentsRetrieve200ResponseSegmentsInnerValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesSegmentsRetrieve200ResponseSegmentsInnerValuesInner from a JSON string
companies_segments_retrieve200_response_segments_inner_values_inner_instance = CompaniesSegmentsRetrieve200ResponseSegmentsInnerValuesInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesSegmentsRetrieve200ResponseSegmentsInnerValuesInner.to_json())

# convert the object into a dict
companies_segments_retrieve200_response_segments_inner_values_inner_dict = companies_segments_retrieve200_response_segments_inner_values_inner_instance.to_dict()
# create an instance of CompaniesSegmentsRetrieve200ResponseSegmentsInnerValuesInner from a dict
companies_segments_retrieve200_response_segments_inner_values_inner_from_dict = CompaniesSegmentsRetrieve200ResponseSegmentsInnerValuesInner.from_dict(companies_segments_retrieve200_response_segments_inner_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


