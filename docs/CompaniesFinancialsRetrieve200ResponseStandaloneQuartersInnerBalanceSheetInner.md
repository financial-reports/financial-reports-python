# CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerBalanceSheetInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** |  | [optional] 
**statement_type** | **str** |  | 
**value** | **str** | Decimal string, absolute units, as served in &#x60;periods&#x60;. | 
**currency** | **str** |  | [optional] 
**basis** | **str** |  | 
**source_filing_ids** | **List[int]** |  | 
**split_adjusted** | [**CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerSplitAdjusted**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerSplitAdjusted.md) |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_standalone_quarters_inner_balance_sheet_inner import CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerBalanceSheetInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerBalanceSheetInner from a JSON string
companies_financials_retrieve200_response_standalone_quarters_inner_balance_sheet_inner_instance = CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerBalanceSheetInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerBalanceSheetInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_standalone_quarters_inner_balance_sheet_inner_dict = companies_financials_retrieve200_response_standalone_quarters_inner_balance_sheet_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerBalanceSheetInner from a dict
companies_financials_retrieve200_response_standalone_quarters_inner_balance_sheet_inner_from_dict = CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerBalanceSheetInner.from_dict(companies_financials_retrieve200_response_standalone_quarters_inner_balance_sheet_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


