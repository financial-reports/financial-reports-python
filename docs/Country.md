# Country


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | English short name from ISO 3166 | 
**alpha_2** | **str** | ISO 3166-1 alpha-2 code (two-letter country code) | 
**alpha_3** | **str** | ISO 3166-1 alpha-3 code (three-letter country code) | 
**numeric** | **str** | ISO 3166-1 numeric code (three-digit country code) | 

## Example

```python
from financial_reports_generated_client.models.country import Country

# TODO update the JSON string below
json = "{}"
# create an instance of Country from a JSON string
country_instance = Country.from_json(json)
# print the JSON string representation of the object
print(Country.to_json())

# convert the object into a dict
country_dict = country_instance.to_dict()
# create an instance of Country from a dict
country_from_dict = Country.from_dict(country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


