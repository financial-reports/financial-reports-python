# CompaniesSeriesRetrieve200ResponseMembersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**method** | **str** | Where the value was read: &#x60;xbrl&#x60; and &#x60;structured&#x60; are the company&#39;s own tagged or structured statements; &#x60;llm&#x60; was read from the report&#39;s text and tables. | [optional] 
**concept** | **str** |  | [optional] 
**link** | **str** | How the member joined, when it is not the first. | [optional] 
**first_period_end** | **date** |  | [optional] 
**last_period_end** | **date** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_series_retrieve200_response_members_inner import CompaniesSeriesRetrieve200ResponseMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesSeriesRetrieve200ResponseMembersInner from a JSON string
companies_series_retrieve200_response_members_inner_instance = CompaniesSeriesRetrieve200ResponseMembersInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesSeriesRetrieve200ResponseMembersInner.to_json())

# convert the object into a dict
companies_series_retrieve200_response_members_inner_dict = companies_series_retrieve200_response_members_inner_instance.to_dict()
# create an instance of CompaniesSeriesRetrieve200ResponseMembersInner from a dict
companies_series_retrieve200_response_members_inner_from_dict = CompaniesSeriesRetrieve200ResponseMembersInner.from_dict(companies_series_retrieve200_response_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


