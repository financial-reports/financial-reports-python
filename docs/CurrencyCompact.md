# CurrencyCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | ISO 4217 currency code (e.g., &#39;USD&#39;, &#39;EUR&#39;). | 
**name** | **str** | Common name of the currency (e.g., &#39;United States Dollar&#39;, &#39;Euro&#39;). | 
**symbol** | **str** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.currency_compact import CurrencyCompact

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyCompact from a JSON string
currency_compact_instance = CurrencyCompact.from_json(json)
# print the JSON string representation of the object
print(CurrencyCompact.to_json())

# convert the object into a dict
currency_compact_dict = currency_compact_instance.to_dict()
# create an instance of CurrencyCompact from a dict
currency_compact_from_dict = CurrencyCompact.from_dict(currency_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


