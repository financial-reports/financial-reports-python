# CompaniesFinancialsRetrieve200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** |  | 
**currency** | [**CompaniesFinancialsRetrieve200ResponseCurrency**](CompaniesFinancialsRetrieve200ResponseCurrency.md) |  | [optional] 
**sources_masked** | **bool** |  | 
**filters** | [**CompaniesFinancialsRetrieve200ResponseFilters**](CompaniesFinancialsRetrieve200ResponseFilters.md) |  | 
**period_count** | **int** |  | 
**periods** | [**List[CompaniesFinancialsRetrieve200ResponsePeriodsInner]**](CompaniesFinancialsRetrieve200ResponsePeriodsInner.md) |  | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response import CompaniesFinancialsRetrieve200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200Response from a JSON string
companies_financials_retrieve200_response_instance = CompaniesFinancialsRetrieve200Response.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200Response.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_dict = companies_financials_retrieve200_response_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200Response from a dict
companies_financials_retrieve200_response_from_dict = CompaniesFinancialsRetrieve200Response.from_dict(companies_financials_retrieve200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


