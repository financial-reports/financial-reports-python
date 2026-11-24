# SavedSearchPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits** | [**List[SavedSearchHit]**](SavedSearchHit.md) |  | 
**saved_search** | [**SavedSearchRef**](SavedSearchRef.md) |  | 
**more** | **int** | New hits past &#x60;max_hits_per_run&#x60;, left for the next runs. A lower bound when &#x60;capped&#x60;. | 
**capped** | **bool** | True: more than the first 1000 matches by relevance fell in the window, so some may never be delivered. Narrow the search. | 
**window** | [**SavedSearchWindow**](SavedSearchWindow.md) |  | 

## Example

```python
from financial_reports_generated_client.models.saved_search_preview import SavedSearchPreview

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSearchPreview from a JSON string
saved_search_preview_instance = SavedSearchPreview.from_json(json)
# print the JSON string representation of the object
print(SavedSearchPreview.to_json())

# convert the object into a dict
saved_search_preview_dict = saved_search_preview_instance.to_dict()
# create an instance of SavedSearchPreview from a dict
saved_search_preview_from_dict = SavedSearchPreview.from_dict(saved_search_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


