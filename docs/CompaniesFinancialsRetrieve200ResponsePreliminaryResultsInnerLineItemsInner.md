# CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInnerLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**value** | **str** | Decimal string, absolute units. | [optional] 
**raw_value** | **str** | As printed, in &#x60;unit&#x60;. | [optional] 
**unit** | **str** | The scale the notice printed, e.g. 억원. | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_preliminary_results_inner_line_items_inner import CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInnerLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInnerLineItemsInner from a JSON string
companies_financials_retrieve200_response_preliminary_results_inner_line_items_inner_instance = CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInnerLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInnerLineItemsInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_preliminary_results_inner_line_items_inner_dict = companies_financials_retrieve200_response_preliminary_results_inner_line_items_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInnerLineItemsInner from a dict
companies_financials_retrieve200_response_preliminary_results_inner_line_items_inner_from_dict = CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInnerLineItemsInner.from_dict(companies_financials_retrieve200_response_preliminary_results_inner_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


