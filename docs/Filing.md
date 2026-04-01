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
**document** | **str** | Direct URL to the raw filing package (e.g., ZIP/PDF) on S3. | [readonly] 
**proxy_url** | **str** | Direct URL to the extracted, browser-renderable main document. | [readonly] 
**viewer_url** | **str** | URL to view the filing in the interactive web platform. | [readonly] 
**file_extension** | **str** | File extension (e.g., PDF, HTML). | [optional] 
**file_size** | **int** | File size in bytes. Stores locally to avoid storage backend hits. | [optional] 
**markdown_url** | **str** |  | [readonly] 
**filing_type_confidence** | **float** | Confidence score (0.0–1.0) assigned by the automated classification system for the filing type. | [readonly] 
**filing_type_reasoning** | **str** | Step-by-step rationale produced by the automated classification system for the assigned filing type. Indicative only — not manually reviewed. | [readonly] 
**fiscal_year** | **int** | The accounting fiscal year this filing covers (e.g., 2024). Populated for annual, quarterly, interim reports and earnings releases. Null if not yet determined. | [readonly] 
**fiscal_period** | [**FiscalPeriodEnum**](FiscalPeriodEnum.md) | The specific fiscal period covered by this filing. Possible values: FY (Full Year), Q1, Q2, Q3, Q4, H1 (First Half), H2 (Second Half). Populated for annual, quarterly, interim reports and earnings releases. Null if not yet determined.  * &#x60;FY&#x60; - Full Year * &#x60;Q1&#x60; - First Quarter * &#x60;Q2&#x60; - Second Quarter * &#x60;Q3&#x60; - Third Quarter * &#x60;Q4&#x60; - Fourth Quarter * &#x60;H1&#x60; - First Half * &#x60;H2&#x60; - Second Half | [readonly] 
**period_ending_date** | **date** | The exact date the reported financial period ends (e.g., 2024-12-31). Populated for annual, quarterly, interim reports and earnings releases. Null if not yet determined. | [readonly] 

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


