# WatchlistResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Indicates the status of the operation (e.g., &#39;success&#39;, &#39;error&#39;). | 
**message** | **str** | A human-readable message describing the outcome. | 
**company_id** | **int** | The ID of the company related to the action, if applicable. | [optional] 

## Example

```python
from financial_reports_generated_client.models.watchlist_response import WatchlistResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WatchlistResponse from a JSON string
watchlist_response_instance = WatchlistResponse.from_json(json)
# print the JSON string representation of the object
print(WatchlistResponse.to_json())

# convert the object into a dict
watchlist_response_dict = watchlist_response_instance.to_dict()
# create an instance of WatchlistResponse from a dict
watchlist_response_from_dict = WatchlistResponse.from_dict(watchlist_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


