# CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** |  | [optional] 
**statement_type** | **str** |  | 
**value** | **str** | Decimal string, absolute units. | 
**currency** | **str** |  | [optional] 
**basis** | **str** |  | 
**formula** | **str** |  | [optional] 
**source_filing_ids** | **List[int]** |  | 
**null_reason** | **str** |  | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_standalone_quarters_inner_line_items_inner import CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerLineItemsInner from a JSON string
companies_financials_retrieve200_response_standalone_quarters_inner_line_items_inner_instance = CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerLineItemsInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_standalone_quarters_inner_line_items_inner_dict = companies_financials_retrieve200_response_standalone_quarters_inner_line_items_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerLineItemsInner from a dict
companies_financials_retrieve200_response_standalone_quarters_inner_line_items_inner_from_dict = CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInnerLineItemsInner.from_dict(companies_financials_retrieve200_response_standalone_quarters_inner_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


