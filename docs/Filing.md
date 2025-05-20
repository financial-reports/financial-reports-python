# Filing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the filing. | [readonly] 
**company** | [**CompanyMinimal**](CompanyMinimal.md) | Basic details of the company that made the filing. | [readonly] 
**filing_type** | [**FilingType**](FilingType.md) | Details of the filing type. | [readonly] 
**language** | [**Language**](Language.md) | Language of the filing document. | [readonly] 
**filing_date** | **date** | The official date the document was filed. | [readonly] 
**title** | **str** | Title of the filing document. | [readonly] 
**added_to_platform** | **datetime** | Timestamp when the filing was added to our system (UTC). | [readonly] 
**updated_date** | **datetime** | Timestamp when the filing record was last updated (UTC). | [readonly] 
**dissemination_datetime** | **datetime** | Timestamp when the filing was disseminated by the source (UTC). | [readonly] 
**release_datetime** | **datetime** | Timestamp when the filing was released (e.g., for press releases) (UTC). | [readonly] 
**source** | [**Source**](Source.md) | Source from which the filing was obtained. | [readonly] 
**document** | **str** | Absolute URL link to the primary filing document (e.g., PDF, HTML). | [readonly] 
**extracted_kpis** | **object** | Stores the structured financial KPIs extracted as JSON. | [readonly] 
**processed_filing_id** | **int** | ID of the processed version of this filing, if available. Null otherwise. | [readonly] 

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


