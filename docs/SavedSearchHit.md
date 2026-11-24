# SavedSearchHit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filing_id** | **str** |  | 
**title** | **str** |  | 
**company** | [**SavedSearchHitCompany**](SavedSearchHitCompany.md) |  | 
**filing_type_code** | **str** |  | 
**release_datetime** | **datetime** |  | 
**added_to_platform** | **datetime** |  | 
**match** | [**OneOf**](OneOf.md) | Snippets, as &#x60;match&#x60; on &#x60;GET /filings/search/&#x60;; null when they were not computed. | 

## Example

```python
from financial_reports_generated_client.models.saved_search_hit import SavedSearchHit

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSearchHit from a JSON string
saved_search_hit_instance = SavedSearchHit.from_json(json)
# print the JSON string representation of the object
print(SavedSearchHit.to_json())

# convert the object into a dict
saved_search_hit_dict = saved_search_hit_instance.to_dict()
# create an instance of SavedSearchHit from a dict
saved_search_hit_from_dict = SavedSearchHit.from_dict(saved_search_hit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


