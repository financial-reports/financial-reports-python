# WatchlistAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | ID of the company. | 

## Example

```python
from financial_reports_generated_client.models.watchlist_action import WatchlistAction

# TODO update the JSON string below
json = "{}"
# create an instance of WatchlistAction from a JSON string
watchlist_action_instance = WatchlistAction.from_json(json)
# print the JSON string representation of the object
print(WatchlistAction.to_json())

# convert the object into a dict
watchlist_action_dict = watchlist_action_instance.to_dict()
# create an instance of WatchlistAction from a dict
watchlist_action_from_dict = WatchlistAction.from_dict(watchlist_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


