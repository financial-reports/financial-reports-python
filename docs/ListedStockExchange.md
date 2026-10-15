# ListedStockExchange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the exchange. | [readonly] 
**name** | **str** | Name of the exchange. | [readonly] 
**ticker** | **str** | Short code of the exchange. | [readonly] 
**website** | **str** | Website of the exchange. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.listed_stock_exchange import ListedStockExchange

# TODO update the JSON string below
json = "{}"
# create an instance of ListedStockExchange from a JSON string
listed_stock_exchange_instance = ListedStockExchange.from_json(json)
# print the JSON string representation of the object
print(ListedStockExchange.to_json())

# convert the object into a dict
listed_stock_exchange_dict = listed_stock_exchange_instance.to_dict()
# create an instance of ListedStockExchange from a dict
listed_stock_exchange_from_dict = ListedStockExchange.from_dict(listed_stock_exchange_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


