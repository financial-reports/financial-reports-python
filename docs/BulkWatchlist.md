# BulkWatchlist


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_ids** | **List[int]** | A list of company IDs (1–100) to add or remove from the watchlist. | 

## Example

```python
from financial_reports_generated_client.models.bulk_watchlist import BulkWatchlist

# TODO update the JSON string below
json = "{}"
# create an instance of BulkWatchlist from a JSON string
bulk_watchlist_instance = BulkWatchlist.from_json(json)
# print the JSON string representation of the object
print(BulkWatchlist.to_json())

# convert the object into a dict
bulk_watchlist_dict = bulk_watchlist_instance.to_dict()
# create an instance of BulkWatchlist from a dict
bulk_watchlist_from_dict = BulkWatchlist.from_dict(bulk_watchlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


