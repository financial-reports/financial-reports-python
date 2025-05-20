# WatchlistCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the company. | [readonly] 
**name** | **str** | The name of the company. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.watchlist_company import WatchlistCompany

# TODO update the JSON string below
json = "{}"
# create an instance of WatchlistCompany from a JSON string
watchlist_company_instance = WatchlistCompany.from_json(json)
# print the JSON string representation of the object
print(WatchlistCompany.to_json())

# convert the object into a dict
watchlist_company_dict = watchlist_company_instance.to_dict()
# create an instance of WatchlistCompany from a dict
watchlist_company_from_dict = WatchlistCompany.from_dict(watchlist_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


