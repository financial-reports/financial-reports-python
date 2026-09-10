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
**language_confidence** | **float** | Confidence score (0.0–1.0) from detecting the language against the document&#39;s own text. Null when detection reached no usable answer, which includes the case where it never ran — use language_verified_at to tell those apart. | [readonly] 
**language_verified_at** | **datetime** | When the language was checked against the document&#39;s own text. Null means it never was: the language is the value asserted when the filing was ingested, which is reliable for a source that files in one language and a guess for one that publishes the same disclosure in several. A non-null value with a null language_confidence means the document was read but no confident answer came out of it. | [readonly] 
**fiscal_year** | **int** | The accounting fiscal year this filing covers (e.g., 2024). Populated for annual, quarterly, interim reports and earnings releases. Null if not yet determined. | [readonly] 
**fiscal_period** | [**FiscalPeriodEnum**](FiscalPeriodEnum.md) | The specific fiscal period covered by this filing. Possible values: FY (Full Year), Q1, Q2, Q3, Q4, H1 (First Half), H2 (Second Half). Populated for annual, quarterly, interim reports and earnings releases. Null if not yet determined.  * &#x60;FY&#x60; - Full Year * &#x60;Q1&#x60; - First Quarter * &#x60;Q2&#x60; - Second Quarter * &#x60;Q3&#x60; - Third Quarter * &#x60;Q4&#x60; - Fourth Quarter * &#x60;H1&#x60; - First Half * &#x60;H2&#x60; - Second Half * &#x60;9M&#x60; - Nine Months | [readonly] 
**period_ending_date** | **date** | The exact date the reported financial period ends (e.g., 2024-12-31). Populated for annual, quarterly, interim reports and earnings releases. Null if not yet determined. | [readonly] 
**ingestion_mode** | [**IngestionModeEnum**](IngestionModeEnum.md) | How this filing entered the platform: REALTIME (picked up within the source&#39;s normal publication-to-availability window) or BACKFILLED (historical import, recovery, or bulk backfill).  * &#x60;REALTIME&#x60; - Realtime * &#x60;BACKFILLED&#x60; - Backfilled | [readonly] 
**source_url** | **str** | Original public link for this filing at the source authority. Null when unavailable, for anonymised sources, or when the account does not have source identities unlocked. | [readonly] 
**source_filing_type** | **str** | The source authority&#39;s own classification label, verbatim. Null when the source publishes no label, it was not captured, or the account does not have source identities unlocked. | [readonly] 
**source_filing_id** | **str** | The publisher&#39;s own identifier for this document, verbatim. Unique per source. On sources that publish one record per event and fan it out into one row per language and per attachment, the leading portion is a shared event stem, so rows of one disclosure sort together -- see the cross-language grouping recipe in the API docs. Null on legacy rows ingested before the identifier was retained. | [readonly] 

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


