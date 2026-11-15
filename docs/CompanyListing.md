# CompanyListing

One equity listing of the company: venue, ticker, FIGI, and whether it is historical.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mic** | **str** | ISO 10383 Market Identifier Code of the venue. | 
**ticker** | **str** | Ticker on that venue, as published with its FIGI. On most venues it is the exchange&#39;s symbol; on Indian venues it is not (&#x60;ICICIBC&#x60;), and the exchange&#39;s is in &#x60;exchange_symbol&#x60;. | 
**exchange_symbol** | **str** | The exchange&#39;s own code where it differs from &#x60;ticker&#x60;: the NSE symbol on XNSE (&#x60;ICICIBANK&#x60;), the numeric BSE scrip code on XBOM (&#x60;532174&#x60;). Null elsewhere and where unknown. | 
**exchange_name** | **str** | Name of the venue. | 
**exch_code** | **str** | Short exchange code, e.g. &#x60;GY&#x60; for Xetra. | 
**security_type** | **str** | Security type, e.g. &#x60;Common Stock&#x60;. | 
**figi** | **str** | Financial Instrument Global Identifier (FIGI) of this listing. | 
**historical** | **bool** | &#x60;true&#x60; when the company is delisted: the line records a venue it used to trade on, not a current one. The ticker may since have been reused by another issuer. | 

## Example

```python
from financial_reports_generated_client.models.company_listing import CompanyListing

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyListing from a JSON string
company_listing_instance = CompanyListing.from_json(json)
# print the JSON string representation of the object
print(CompanyListing.to_json())

# convert the object into a dict
company_listing_dict = company_listing_instance.to_dict()
# create an instance of CompanyListing from a dict
company_listing_from_dict = CompanyListing.from_dict(company_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


