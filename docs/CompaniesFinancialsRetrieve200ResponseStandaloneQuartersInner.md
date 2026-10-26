# CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**fiscal_year** | **int** |  | 
**fiscal_period** | **str** |  | 
**period_start_date** | **date** |  | 
**period_end_date** | **date** |  | 
**line_items** | [**List[CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerLineItemsInner]**](CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerLineItemsInner.md) |  | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_standalone_quarters_inner import CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInner from a JSON string
companies_financials_retrieve200_response_standalone_quarters_inner_instance = CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_standalone_quarters_inner_dict = companies_financials_retrieve200_response_standalone_quarters_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInner from a dict
companies_financials_retrieve200_response_standalone_quarters_inner_from_dict = CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInner.from_dict(companies_financials_retrieve200_response_standalone_quarters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


