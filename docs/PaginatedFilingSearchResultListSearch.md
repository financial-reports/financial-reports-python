# PaginatedFilingSearchResultListSearch

About the full-text candidate set. `count` is the number of matching filings you can see among those this endpoint pages, at most `max_results`. Visibility is checked against the index's candidates in relevance order, up to a scan limit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capped** | **bool** | True: more matching filings MAY exist beyond what this endpoint pages, either because more than &#x60;max_results&#x60; are visible or because the scan stopped early (&#x60;scan_complete&#x60; false). False: &#x60;count&#x60; is every match you can see. | [optional] 
**scan_complete** | **bool** | True: every candidate the index matched was checked. False: the scan stopped (a scan limit or time budget) before checking every candidate. An EMPTY page with &#x60;scan_complete&#x60; false is NOT an absence, and more matching filings may exist; &#x60;count&#x60; is then a lower bound (what the scan found), not the visible total: narrow &#x60;q&#x60; or the filters and search again. | [optional] 
**max_results** | **int** |  | [optional] 
**scope** | **str** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.paginated_filing_search_result_list_search import PaginatedFilingSearchResultListSearch

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFilingSearchResultListSearch from a JSON string
paginated_filing_search_result_list_search_instance = PaginatedFilingSearchResultListSearch.from_json(json)
# print the JSON string representation of the object
print(PaginatedFilingSearchResultListSearch.to_json())

# convert the object into a dict
paginated_filing_search_result_list_search_dict = paginated_filing_search_result_list_search_instance.to_dict()
# create an instance of PaginatedFilingSearchResultListSearch from a dict
paginated_filing_search_result_list_search_from_dict = PaginatedFilingSearchResultListSearch.from_dict(paginated_filing_search_result_list_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


