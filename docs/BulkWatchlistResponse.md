# BulkWatchlistResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Indicates the status of the operation (e.g., &#39;success&#39;, &#39;error&#39;). | 
**message** | **str** | A human-readable message describing the outcome. | 
**company_ids** | **List[int]** | The IDs of the companies affected by the action. | [optional] 

## Example

```python
from financial_reports_generated_client.models.bulk_watchlist_response import BulkWatchlistResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkWatchlistResponse from a JSON string
bulk_watchlist_response_instance = BulkWatchlistResponse.from_json(json)
# print the JSON string representation of the object
print(BulkWatchlistResponse.to_json())

# convert the object into a dict
bulk_watchlist_response_dict = bulk_watchlist_response_instance.to_dict()
# create an instance of BulkWatchlistResponse from a dict
bulk_watchlist_response_from_dict = BulkWatchlistResponse.from_dict(bulk_watchlist_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


