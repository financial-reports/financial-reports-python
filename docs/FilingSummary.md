# FilingSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**title** | **str** | Optional title for the filing | [optional] 
**release_datetime** | **datetime** | Time the document was published on the authority page | [optional] 
**company** | [**CompanyMinimal**](CompanyMinimal.md) |  | [readonly] 
**filing_type** | [**FilingType**](FilingType.md) |  | [readonly] 
**processing_status** | [**ProcessingStatusEnum**](ProcessingStatusEnum.md) | The lifecycle status of the raw document to markdown conversion.  * &#x60;PENDING&#x60; - Pending * &#x60;QUEUED&#x60; - Queued * &#x60;PROCESSING&#x60; - Processing * &#x60;COMPLETED&#x60; - Completed * &#x60;FAILED&#x60; - Failed * &#x60;SKIPPED&#x60; - Skipped | [optional] 
**file_extension** | **str** | File extension (e.g., PDF, HTML). | [optional] 
**file_size** | **int** | File size in bytes. Stores locally to avoid storage backend hits. | [optional] 

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


