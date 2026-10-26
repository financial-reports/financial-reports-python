# CompaniesSegmentsRetrieve200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** |  | 
**filters** | [**CompaniesSegmentsRetrieve200ResponseFilters**](CompaniesSegmentsRetrieve200ResponseFilters.md) |  | 
**segments** | [**List[CompaniesSegmentsRetrieve200ResponseSegmentsInner]**](CompaniesSegmentsRetrieve200ResponseSegmentsInner.md) |  | 
**history_window** | [**CompaniesFinancialsRetrieve200ResponseHistoryWindow**](CompaniesFinancialsRetrieve200ResponseHistoryWindow.md) |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_segments_retrieve200_response import CompaniesSegmentsRetrieve200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesSegmentsRetrieve200Response from a JSON string
companies_segments_retrieve200_response_instance = CompaniesSegmentsRetrieve200Response.from_json(json)
# print the JSON string representation of the object
print(CompaniesSegmentsRetrieve200Response.to_json())

# convert the object into a dict
companies_segments_retrieve200_response_dict = companies_segments_retrieve200_response_instance.to_dict()
# create an instance of CompaniesSegmentsRetrieve200Response from a dict
companies_segments_retrieve200_response_from_dict = CompaniesSegmentsRetrieve200Response.from_dict(companies_segments_retrieve200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


