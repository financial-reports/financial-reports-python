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
**historical** | **bool** | &#x60;true&#x60; when the company is delisted: the line records a venue it used to trade on, not a current one. The ticker may since have been reused by another issuer. | [readonly] 
**exchange_symbol** | **str** | The exchange&#39;s own code where it differs from &#x60;ticker&#x60;: the NSE symbol on XNSE (&#x60;ICICIBANK&#x60;), the numeric BSE scrip code on XBOM (&#x60;532174&#x60;), the Bursa Malaysia stock code on XKLS (&#x60;1155&#x60;), the SGX code on XSES (&#x60;D05&#x60;). Empty elsewhere and where unknown. | [readonly] 

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


