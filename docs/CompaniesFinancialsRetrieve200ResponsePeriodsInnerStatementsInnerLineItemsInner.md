# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** |  | 
**statement_type** | **str** | The KPI&#39;s home statement in the taxonomy, which can differ from the statement it was extracted onto. &#x60;SUP&#x60; appears here but is never a statement type. | 
**depth** | **int** |  | 
**parent_code** | **str** |  | 
**sort_order** | **int** |  | 
**value** | **decimal.Decimal** | Value in absolute units, as an exact decimal string, not a number. Parse with a decimal type; float loses precision at financial magnitudes. Null when the figure was withheld as unrecoverable. | 
**raw_value** | **decimal.Decimal** | The figure as printed in the document, as an exact decimal string. When non-null, &#x60;value &#x3D;&#x3D; raw_value * multiplier(scale)&#x60; to rounding (within 1% or 0.01). Null, together with &#x60;scale&#x60;, when &#x60;value&#x60; is null, when &#x60;value&#x60; was computed from other line items rather than read from the document (e.g. &#x60;net_debt&#x60; recomputed from the figures served beside it), or whenever &#x60;raw_value * scale&#x60; does not reproduce &#x60;value&#x60; (e.g. a value rescaled against the company&#39;s other filings), because then the printed figure is no longer the value&#39;s provenance. A printed total that is missing some of its components keeps its &#x60;raw_value&#x60;, because the printed figure is still its provenance. | 
**scale** | **str** | Reporting scale of &#x60;raw_value&#x60;. Withheld with it. | 
**currency** | **str** | The value&#39;s own currency code, which may differ from the statement&#39;s reporting currency for per-share figures. Null for ratios. | 
**confidence** | **float** | Confidence that this value is the figure the document states, or null where nothing has judged it. Non-null only where a second, independent check of the filing agreed with the extracted value; the number is that check&#39;s probability for the figure it picked. Null does not mean low confidence: it means unjudged, which is every value not yet checked and every value sent for review. Treat it as a filter, not a score: branch on non-null, do not compare nulls. | 
**source_page** | **int** | The 1-based page of the source filing&#39;s PDF the value is printed on, for a value read from the PDF rather than from XBRL. Null when it is not known: the document is not a PDF (XBRL, HTML), the value could not be placed on exactly one page, or the value served is computed or withheld rather than the printed figure (&#x60;raw_value&#x60; is then null too). | 
**revisions** | [**List[CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerRevisionsInner]**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerRevisionsInner.md) | Present only with &#x60;include&#x3D;revisions&#x60;: every recorded change to this value, oldest first (with &#x60;as_known_at&#x60;, up to that time). Empty when none was recorded. Recording started 2026-10-19T17:05:18Z; &#x60;pre_recording&#x60; entries are older corrections whose &#x60;changed_at&#x60; is approximate (the change happened at or before it). | [optional] 
**withdrawn_reason** | **str** | Present only with &#x60;as_known_at&#x60;, and only on a statement (and on its values) that was served for this company at that time and is not served for it today because it was withdrawn: &#x60;reattributed&#x60;: the statement now belongs to another company record, where it may be served; &#x60;purged&#x60;: reserved, its filing was removed altogether (not served yet; the filing&#39;s type, release time and links would be null unless recorded). Absent everywhere else. | [optional] 
**as_reported** | [**CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReported**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerAsReported.md) |  | [optional] 
**split_adjusted** | [**CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerSplitAdjusted**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInnerSplitAdjusted.md) |  | [optional] 
**updated_at** | **datetime** | When this value was last written. Equal to the extraction time for an untouched value; moves when a later correction pass rewrites the value in place (a re-extraction replaces the whole statement and sets a new one). Compare it with the value from your previous poll to detect a changed figure without diffing. It does not move when a whole statement is withdrawn or when a different filing starts supplying the period; watch &#x60;source_filing&#x60; for that. | 
**available_at** | **datetime** | When the filing this value was read from was released. Usually the statement&#39;s own &#x60;source_filing.release_datetime&#x60;. Later where the value was filled in from another filing because the selected statement lacks it (named in &#x60;extraction.notes&#x60;): for example a prior-year figure taken from the next annual report. For a point-in-time series, drop values whose &#x60;available_at&#x60; is after your cutoff, or pass &#x60;as_of&#x60;, which never serves a value from a filing released after it. | 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner import CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner from a JSON string
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_dict = companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner from a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner.from_dict(companies_financials_retrieve200_response_periods_inner_statements_inner_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


