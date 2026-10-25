# CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_type** | **str** |  | 
**statement_type_display** | **str** |  | 
**currency** | [**CompaniesFinancialsRetrieve200ResponseCurrency**](CompaniesFinancialsRetrieve200ResponseCurrency.md) |  | 
**currency_mismatch** | **bool** | True when this statement&#39;s currency differs from the company&#39;s modal reporting currency - the code held by more than 60% of the statements we serve for that company. When no code clears 60% (a genuinely dual-currency issuer, or one mid-transition) there is no modal currency and this is &#x60;false&#x60; on every statement, including the off-currency ones. A data-quality signal, not provenance, so it is returned even to masked accounts. It compares a statement against its company&#39;s history; it does not mean the statement itself mixes currencies. | 
**accounting_standard** | **str** | The accounting standard the statement was prepared under. National standards that are IFRS word for word (K-IFRS, TIFRS, HKFRS, SFRS(I), AASB, ...) are &#x60;IFRS&#x60;; ones with carve-outs or only converged (Ind AS, CAS, SAK, JMIS, any national GAAP) are &#x60;LOCAL_GAAP&#x60;. &#x60;UNKNOWN&#x60; when neither the filing nor its market says; null on statements not yet classified. See &#x60;accounting_standard_basis&#x60; for how it is known. | [optional] 
**accounting_standard_basis** | **str** | How &#x60;accounting_standard&#x60; is known. &#x60;xbrl_taxonomy&#x60;: read from the filing&#39;s own XBRL (a declared standard, or the standard taxonomy its facts are tagged in). &#x60;market_default&#x60;: not read from the filing; the standard listed companies in its home market must use for consolidated accounts, so an issuer with an exemption may differ. &#x60;filer_stated&#x60; and &#x60;document_stated&#x60; are reserved. Null when the standard is &#x60;UNKNOWN&#x60; or not yet classified. | [optional] 
**extraction** | [**CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerExtraction**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerExtraction.md) |  | 
**line_items** | [**List[CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner]**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerLineItemsInner.md) |  | 
**withdrawn_reason** | **str** | Present only with &#x60;as_known_at&#x60;, and only on a statement (and on its values) that was served for this company at that time and is not served for it today because it was withdrawn: &#x60;reattributed&#x60; - the statement now belongs to another company record, where it may be served; &#x60;purged&#x60; - reserved: its filing was removed altogether (not served yet; the filing&#39;s type, release time and links would be null unless recorded). Absent everywhere else. | [optional] 
**is_comparative** | **bool** | True when this period was read from the comparative (prior-year) column of a later report, because no report presented it as its own period. A data-quality signal, not provenance, so it is returned even to masked accounts. | 
**source_filing** | [**CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourceFiling**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourceFiling.md) |  | [optional] 
**sources** | [**List[CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourcesInner]**](CompaniesFinancialsRetrieve200ResponsePeriodsInnerStatementsInnerSourcesInner.md) | Every filing that reported this (period, statement_type), including the candidates selection rejected and any filing whose values filled in the selected statement. Omitted unless the account has source unmasking. The selected filing is always available as &#x60;source_filing&#x60;. | [optional] 

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


