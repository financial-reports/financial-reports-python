# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_type** | **str** |  | 
**statement_type_display** | **str** |  | 
**currency** | [**CompaniesFinancialsRetrieve200ResponseCurrency**](CompaniesFinancialsRetrieve200ResponseCurrency.md) |  | 
**currency_mismatch** | **bool** | True when this statement&#39;s currency differs from the company&#39;s modal reporting currency. A data-quality signal, not provenance, so it is returned even to masked accounts. | 
**extraction** | [**CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerExtraction**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerExtraction.md) |  | 
**line_items** | [**List[CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner]**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner.md) |  | 
**is_comparative** | **bool** | True when this period was read from the comparative (prior-year) column of a later report, because no report presented it as its own period. A data-quality signal, not provenance, so it is returned even to masked accounts. | 
**source_filing** | [**CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourceFiling**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourceFiling.md) |  | [optional] 
**sources** | [**List[CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourcesInner]**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourcesInner.md) | Every filing that reported this (period, statement_type), including the candidates selection rejected. Omitted unless the account has source unmasking. The selected filing is always available as &#x60;source_filing&#x60;. | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response_periods_inner_statements_inner import CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInner from a JSON string
companies_financials_retrieve200_response_periods_inner_statements_inner_instance = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInner.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInner.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_dict = companies_financials_retrieve200_response_periods_inner_statements_inner_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInner from a dict
companies_financials_retrieve200_response_periods_inner_statements_inner_from_dict = CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInner.from_dict(companies_financials_retrieve200_response_periods_inner_statements_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


