# CompaniesFinancialsRetrieve200ResponseRatiosInnerRatiosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** |  | 
**value** | **str** | Decimal string, 6 decimal places. | 
**currency** | **str** |  | 
**null_reason** | **str** |  | 
**missing_inputs** | **List[str]** |  | 
**formula** | **str** |  | 
**inputs** | **Dict[str, str]** |  | 
**source_filing_ids** | **List[int]** |  | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_ratios_inner_ratios_inner import CompaniesFinancialsRetrieve200ResponseRatiosInnerRatiosInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponseRatiosInnerRatiosInner from a JSON string
companies_financials_retrieve200_response_ratios_inner_ratios_inner_instance = CompaniesFinancialsRetrieve200ResponseRatiosInnerRatiosInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponseRatiosInnerRatiosInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_ratios_inner_ratios_inner_dict = companies_financials_retrieve200_response_ratios_inner_ratios_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponseRatiosInnerRatiosInner from a dict
companies_financials_retrieve200_response_ratios_inner_ratios_inner_from_dict = CompaniesFinancialsRetrieve200ResponseRatiosInnerRatiosInner.from_dict(companies_financials_retrieve200_response_ratios_inner_ratios_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


