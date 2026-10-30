# CompaniesFinancialsRetrieve200ResponseRatiosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fiscal_year** | **int** |  | 
**fiscal_period** | **str** |  | 
**period_end_date** | **date** |  | 
**ratios** | [**List[CompaniesFinancialsRetrieve200ResponseRatiosInnerRatiosInner]**](CompaniesFinancialsRetrieve200ResponseRatiosInnerRatiosInner.md) |  | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_ratios_inner import CompaniesFinancialsRetrieve200ResponseRatiosInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponseRatiosInner from a JSON string
companies_financials_retrieve200_response_ratios_inner_instance = CompaniesFinancialsRetrieve200ResponseRatiosInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponseRatiosInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_ratios_inner_dict = companies_financials_retrieve200_response_ratios_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponseRatiosInner from a dict
companies_financials_retrieve200_response_ratios_inner_from_dict = CompaniesFinancialsRetrieve200ResponseRatiosInner.from_dict(companies_financials_retrieve200_response_ratios_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


