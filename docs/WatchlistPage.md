# WatchlistPage

Paginated watchlist envelope: the standard GlobalCustomPagination fields plus the `is_locked` flag the watchlist view appends to the page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of companies on the watchlist. | 
**next** | **str** | URL of the next page of results, or null on the last page. | 
**previous** | **str** | URL of the previous page of results, or null on the first page. | 
**results** | [**List[WatchlistCompany]**](WatchlistCompany.md) | Companies on the current page. | 
**is_locked** | **bool** | Whether the watchlist is locked by an administrator. | 

## Example

```python
from financial_reports_generated_client.models.watchlist_page import WatchlistPage

# TODO update the JSON string below
json = "{}"
# create an instance of WatchlistPage from a JSON string
watchlist_page_instance = WatchlistPage.from_json(json)
# print the JSON string representation of the object
print(WatchlistPage.to_json())

# convert the object into a dict
watchlist_page_dict = watchlist_page_instance.to_dict()
# create an instance of WatchlistPage from a dict
watchlist_page_from_dict = WatchlistPage.from_dict(watchlist_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


