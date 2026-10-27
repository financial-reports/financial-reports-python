# CompaniesDividendsRetrieve200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** |  | 
**filters** | [**CompaniesDividendsRetrieve200ResponseFilters**](CompaniesDividendsRetrieve200ResponseFilters.md) |  | 
**dividends** | [**List[CompaniesDividendsRetrieve200ResponseDividendsInner]**](CompaniesDividendsRetrieve200ResponseDividendsInner.md) |  | 
**history_window** | **object** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_dividends_retrieve200_response import CompaniesDividendsRetrieve200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesDividendsRetrieve200Response from a JSON string
companies_dividends_retrieve200_response_instance = CompaniesDividendsRetrieve200Response.from_json(json)
# print the JSON string representation of the object
print(CompaniesDividendsRetrieve200Response.to_json())

# convert the object into a dict
companies_dividends_retrieve200_response_dict = companies_dividends_retrieve200_response_instance.to_dict()
# create an instance of CompaniesDividendsRetrieve200Response from a dict
companies_dividends_retrieve200_response_from_dict = CompaniesDividendsRetrieve200Response.from_dict(companies_dividends_retrieve200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


