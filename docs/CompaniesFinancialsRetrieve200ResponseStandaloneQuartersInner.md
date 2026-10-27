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
**balance_sheet** | [**List[CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerBalanceSheetInner]**](CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerBalanceSheetInner.md) | The balance sheet &#x60;periods&#x60; serves at this period&#39;s &#x60;period_end_date&#x60;, as reported (a balance sheet is never derived). &#x60;periods&#x60; serves one balance sheet per date, under the longest period ending on it, so a US quarterly report&#39;s is there under &#x60;H1&#x60; or &#x60;9M&#x60;; here it is on &#x60;Q2&#x60; or &#x60;Q3&#x60;. Empty when no balance sheet is served at that date. | [optional] 

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


