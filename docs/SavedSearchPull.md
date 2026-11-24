# SavedSearchPull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits** | [**List[SavedSearchHit]**](SavedSearchHit.md) |  | 
**saved_search** | [**SavedSearchPullRef**](SavedSearchPullRef.md) |  | 
**more** | **int** | New hits past &#x60;max_hits_per_run&#x60;, left for the next pulls: pull again now to get them. A lower bound when &#x60;capped&#x60;. | 
**capped** | **bool** | True: more than the first 1000 matches by relevance fell in the window, so some may never be returned. Narrow the search. | 
**scan_complete** | **bool** | False: the search stopped before checking every candidate, so more new filings may exist than were returned. With no hits, nothing was recorded; pull again later. | 
**window** | [**SavedSearchPullWindow**](SavedSearchPullWindow.md) |  | 
**pulled_at** | **datetime** | Only with &#x60;repeat_last_pull&#x3D;true&#x60;: when that pull ran (null: no pull has returned hits yet). That response carries &#x60;saved_search&#x60;, &#x60;hits&#x60; and &#x60;pulled_at&#x60; only. | [optional] 

## Example

```python
from financial_reports_generated_client.models.saved_search_pull import SavedSearchPull

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSearchPull from a JSON string
saved_search_pull_instance = SavedSearchPull.from_json(json)
# print the JSON string representation of the object
print(SavedSearchPull.to_json())

# convert the object into a dict
saved_search_pull_dict = saved_search_pull_instance.to_dict()
# create an instance of SavedSearchPull from a dict
saved_search_pull_from_dict = SavedSearchPull.from_dict(saved_search_pull_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


