# PaginatedFilingSearchResultList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total matching results. Exact for cheap queries, an estimate on broad or expensive ones. Do not use it to decide when to stop: follow &#x60;next&#x60; until it is null. | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FilingSearchResult]**](FilingSearchResult.md) |  | 
**history_window** | [**PaginatedFilingSearchResultListHistoryWindow**](PaginatedFilingSearchResultListHistoryWindow.md) |  | [optional] 
**search** | [**PaginatedFilingSearchResultListSearch**](PaginatedFilingSearchResultListSearch.md) |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.paginated_filing_search_result_list import PaginatedFilingSearchResultList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFilingSearchResultList from a JSON string
paginated_filing_search_result_list_instance = PaginatedFilingSearchResultList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFilingSearchResultList.to_json())

# convert the object into a dict
paginated_filing_search_result_list_dict = paginated_filing_search_result_list_instance.to_dict()
# create an instance of PaginatedFilingSearchResultList from a dict
paginated_filing_search_result_list_from_dict = PaginatedFilingSearchResultList.from_dict(paginated_filing_search_result_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


