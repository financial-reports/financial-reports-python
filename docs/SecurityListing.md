# SecurityListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**company** | [**CompanyMinimal**](CompanyMinimal.md) |  | [readonly] 
**mic** | **str** |  | [readonly] 
**ticker** | **str** |  | [readonly] 
**exch_code** | **str** |  | [readonly] 
**exchange_name** | **str** | Display name of the exchange, when the MIC maps to a known venue. | [readonly] 
**security_type** | **str** |  | [readonly] 
**market_sector** | **str** |  | [readonly] 
**figi** | **str** |  | [readonly] 
**composite_figi** | **str** |  | [readonly] 
**share_class_figi** | **str** |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.security_listing import SecurityListing

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityListing from a JSON string
security_listing_instance = SecurityListing.from_json(json)
# print the JSON string representation of the object
print(SecurityListing.to_json())

# convert the object into a dict
security_listing_dict = security_listing_instance.to_dict()
# create an instance of SecurityListing from a dict
security_listing_from_dict = SecurityListing.from_dict(security_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


