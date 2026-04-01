# ISIN


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The 12-character International Securities Identification Number. | [readonly] 
**is_primary** | **bool** | Indicates if this is the primary ISIN for the company on this platform. | [readonly] 
**company** | [**CompanyMinimal**](CompanyMinimal.md) | The company associated with this ISIN. | [readonly] 
**figi** | **str** | The 12-character Financial Instrument Global Identifier (FIGI) for this specific listing. | [readonly] 
**composite_figi** | **str** | The composite FIGI representing the instrument across all exchanges in a given country. | [readonly] 
**share_class_figi** | **str** | The share class FIGI representing the instrument globally, regardless of exchange. | [readonly] 
**security_type** | **str** | Primary security type classification (e.g., Common Stock, ETP, REIT). | [readonly] 
**security_type2** | **str** | Secondary security type classification providing additional granularity. | [readonly] 
**market_sector** | **str** | Market sector classification from OpenFIGI (e.g., Equity, Govt, Corp). | [readonly] 
**exch_code** | **str** | Exchange code where this security is listed (e.g., GY, US, LN). | [readonly] 
**figi_last_updated** | **datetime** | Timestamp of the last successful FIGI data enrichment for this ISIN. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.isin import ISIN

# TODO update the JSON string below
json = "{}"
# create an instance of ISIN from a JSON string
isin_instance = ISIN.from_json(json)
# print the JSON string representation of the object
print(ISIN.to_json())

# convert the object into a dict
isin_dict = isin_instance.to_dict()
# create an instance of ISIN from a dict
isin_from_dict = ISIN.from_dict(isin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


