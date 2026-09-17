# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourceFiling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**filing_type** | **str** | Our own normalised filing-type code, not the publishing authority&#39;s label. | [optional] 
**release_datetime** | **datetime** |  | [optional] 
**document_url** | **str** | Direct link to our hosted copy of the document. Null in the rare case we hold no document for the filing. | [optional] 
**viewer_url** | **str** | Link to the document on our own platform. | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner_statements_inner_source_filing import CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourceFiling

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourceFiling from a JSON string
companies_financials_retrieve200_response_periods_inner_statements_inner_source_filing_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourceFiling.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourceFiling.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_source_filing_dict = companies_financials_retrieve200_response_periods_inner_statements_inner_source_filing_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourceFiling from a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_source_filing_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourceFiling.from_dict(companies_financials_retrieve200_response_periods_inner_statements_inner_source_filing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


