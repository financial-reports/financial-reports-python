# CompanyListing

Inline schema type for the curated `listings[]` array on CompanySerializer.  These 6 fields are what ``CompanySerializer.get_listings`` returns — a de-duplicated, equity-only subset of ``SecurityListing`` rows.  Using an explicit serializer here (rather than ``SecurityListingSerializer``) keeps the OpenAPI contract tight and avoids advertising the 11-field full model shape that includes ``company``, ``market_sector``, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mic** | **str** | ISO 10383 Market Identifier Code of the venue. | 
**ticker** | **str** | Ticker on that venue. | 
**exchange_name** | **str** | Name of the venue. | 
**exch_code** | **str** | Short exchange code, e.g. &#x60;GY&#x60; for Xetra. | 
**security_type** | **str** | Security type, e.g. &#x60;Common Stock&#x60;. | 
**figi** | **str** | Financial Instrument Global Identifier (FIGI) of this listing. | 

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


