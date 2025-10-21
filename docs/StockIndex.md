# StockIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [readonly] 
**ticker** | **str** |  | [readonly] 
**isin** | **str** |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.stock_index import StockIndex

# TODO update the JSON string below
json = "{}"
# create an instance of StockIndex from a JSON string
stock_index_instance = StockIndex.from_json(json)
# print the JSON string representation of the object
print(StockIndex.to_json())

# convert the object into a dict
stock_index_dict = stock_index_instance.to_dict()
# create an instance of StockIndex from a dict
stock_index_from_dict = StockIndex.from_dict(stock_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


