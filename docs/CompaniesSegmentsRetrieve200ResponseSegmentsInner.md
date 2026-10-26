# CompaniesSegmentsRetrieve200ResponseSegmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**axis** | **str** |  | 
**name** | **str** |  | 
**values** | [**List[CompaniesSegmentsRetrieve200ResponseSegmentsInnerValuesInner]**](CompaniesSegmentsRetrieve200ResponseSegmentsInnerValuesInner.md) |  | 

## Example

```python
from financial_reports_generated_client.models.companies_segments_retrieve200_response_segments_inner import CompaniesSegmentsRetrieve200ResponseSegmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesSegmentsRetrieve200ResponseSegmentsInner from a JSON string
companies_segments_retrieve200_response_segments_inner_instance = CompaniesSegmentsRetrieve200ResponseSegmentsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesSegmentsRetrieve200ResponseSegmentsInner.to_json())

# convert the object into a dict
companies_segments_retrieve200_response_segments_inner_dict = companies_segments_retrieve200_response_segments_inner_instance.to_dict()
# create an instance of CompaniesSegmentsRetrieve200ResponseSegmentsInner from a dict
companies_segments_retrieve200_response_segments_inner_from_dict = CompaniesSegmentsRetrieve200ResponseSegmentsInner.from_dict(companies_segments_retrieve200_response_segments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


