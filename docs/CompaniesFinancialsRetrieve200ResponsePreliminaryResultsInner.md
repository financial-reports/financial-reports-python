# CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**fiscal_period** | **str** |  | [optional] 
**period_start_date** | **date** |  | [optional] 
**period_end_date** | **date** |  | [optional] 
**basis** | **str** |  | [optional] 
**is_correction** | **bool** |  | [optional] 
**is_latest** | **bool** |  | [optional] 
**source_filing** | [**CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInnerSourceFiling**](CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInnerSourceFiling.md) |  | [optional] 
**line_items** | [**List[CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInnerLineItemsInner]**](CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInnerLineItemsInner.md) |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_preliminary_results_inner import CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInner from a JSON string
companies_financials_retrieve200_response_preliminary_results_inner_instance = CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_preliminary_results_inner_dict = companies_financials_retrieve200_response_preliminary_results_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInner from a dict
companies_financials_retrieve200_response_preliminary_results_inner_from_dict = CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInner.from_dict(companies_financials_retrieve200_response_preliminary_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


