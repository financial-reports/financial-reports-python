# PaginatedFilingSearchResultListSearchTypesResolvedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**param** | **str** |  | [optional] 
**requested** | **str** | The code you sent, upper-cased. | [optional] 
**types** | **List[str]** | The FinancialFilings type codes it was searched as. | [optional] 
**widens** | **bool** | True: those types also hold filings that are not the code you sent, so the search may match more than you asked for. | [optional] 
**may_miss** | **bool** | True: some filings of that form are classified under a more specific type that is not included. | [optional] 
**note** | **str** | The same, in words. | [optional] 

## Example

```python
from financial_reports_generated_client.models.paginated_filing_search_result_list_search_types_resolved_inner import PaginatedFilingSearchResultListSearchTypesResolvedInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFilingSearchResultListSearchTypesResolvedInner from a JSON string
paginated_filing_search_result_list_search_types_resolved_inner_instance = PaginatedFilingSearchResultListSearchTypesResolvedInner.from_json(json)
# print the JSON string representation of the object
print(PaginatedFilingSearchResultListSearchTypesResolvedInner.to_json())

# convert the object into a dict
paginated_filing_search_result_list_search_types_resolved_inner_dict = paginated_filing_search_result_list_search_types_resolved_inner_instance.to_dict()
# create an instance of PaginatedFilingSearchResultListSearchTypesResolvedInner from a dict
paginated_filing_search_result_list_search_types_resolved_inner_from_dict = PaginatedFilingSearchResultListSearchTypesResolvedInner.from_dict(paginated_filing_search_result_list_search_types_resolved_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


