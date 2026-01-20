# Filing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**company** | [**CompanyMinimal**](CompanyMinimal.md) |  | [readonly] 
**filing_type** | [**FilingType**](FilingType.md) |  | [readonly] 
**language** | [**Language**](Language.md) |  | [readonly] 
**filing_date** | **date** | The official date of the filing (soon to be deprecated). | 
**title** | **str** | Optional title for the filing | [optional] 
**added_to_platform** | **datetime** | Date and time when the filing was added to our platform | [readonly] 
**updated_date** | **datetime** | The date and time this filing record was last modified. | [readonly] 
**dissemination_datetime** | **datetime** | Time the document was released to the public and sent to the authority | [optional] 
**release_datetime** | **datetime** | Time the document was published on the authority page | [optional] 
**source** | [**Source**](Source.md) |  | [readonly] 
**document** | **str** |  | [readonly] 
**file_extension** | **str** | File extension (e.g., PDF, HTML). | [optional] 
**file_size** | **int** | File size in bytes. Stores locally to avoid storage backend hits. | [optional] 
**markdown_url** | **str** |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.filing import Filing

# TODO update the JSON string below
json = "{}"
# create an instance of Filing from a JSON string
filing_instance = Filing.from_json(json)
# print the JSON string representation of the object
print(Filing.to_json())

# convert the object into a dict
filing_dict = filing_instance.to_dict()
# create an instance of Filing from a dict
filing_from_dict = Filing.from_dict(filing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


