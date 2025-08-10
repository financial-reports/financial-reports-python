# FilingSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**title** | **str** | Optional title for the filing | [optional] 
**release_datetime** | **datetime** | Time the document was published on the authority page | [optional] 
**company** | [**CompanyMinimal**](CompanyMinimal.md) |  | [readonly] 
**filing_type** | [**FilingType**](FilingType.md) |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.filing_summary import FilingSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FilingSummary from a JSON string
filing_summary_instance = FilingSummary.from_json(json)
# print the JSON string representation of the object
print(FilingSummary.to_json())

# convert the object into a dict
filing_summary_dict = filing_summary_instance.to_dict()
# create an instance of FilingSummary from a dict
filing_summary_from_dict = FilingSummary.from_dict(filing_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


