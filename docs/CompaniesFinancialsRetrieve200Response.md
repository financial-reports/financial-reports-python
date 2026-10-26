# CompaniesFinancialsRetrieve200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** |  | 
**template** | **str** | The company&#39;s KPI template. Banks and insurers also get their template&#39;s own line items; see &#x60;templates&#x60; on /api/line-item-definitions/ for which items are meaningful for it. | [optional] 
**currency** | [**CompaniesFinancialsRetrieve200ResponseCurrency**](CompaniesFinancialsRetrieve200ResponseCurrency.md) |  | [optional] 
**sources_masked** | **bool** |  | 
**filters** | [**CompaniesFinancialsRetrieve200ResponseFilters**](CompaniesFinancialsRetrieve200ResponseFilters.md) |  | 
**period_count** | **int** |  | 
**periods** | [**List[CompaniesFinancialsRetrieve200ResponsePeriodsInner]**](CompaniesFinancialsRetrieve200ResponsePeriodsInner.md) |  | 
**notice** | **str** |  | [optional] 
**history_window** | [**CompaniesFinancialsRetrieve200ResponseHistoryWindow**](CompaniesFinancialsRetrieve200ResponseHistoryWindow.md) |  | [optional] 
**preliminary_results** | [**List[CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInner]**](CompaniesFinancialsRetrieve200ResponsePreliminaryResultsInner.md) | Present only with &#x60;include&#x3D;preliminary&#x60;. The company&#39;s own preliminary results figures, published before the report for the period and expected to differ from it (today: Korean 잠정실적 notices). Never merged into &#x60;periods&#x60;. One entry per notice and period, corrections included, so the history is point in time: &#x60;is_latest&#x60; marks the newest notice for its period and basis among those returned. | [optional] 
**standalone_quarters** | [**List[CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInner]**](CompaniesFinancialsRetrieve200ResponseStandaloneQuartersInner.md) | Present only with &#x60;include&#x3D;standalone_quarters&#x60;. One three-month period per fiscal quarter (a six-month &#x60;H2&#x60; for a company that reports half years only), income statement and cash flow only, newest first. &#x60;reported&#x60; values are the company&#39;s own three-month figures; &#x60;derived&#x60; values are differences of its reported year-to-date figures (&#x60;formula&#x60;, e.g. &#x60;H1 - Q1&#x60;, and the &#x60;source_filing_ids&#x60; they rest on); &#x60;derived_approx&#x60; is EPS as the difference of year-to-date EPS, given only when the weighted share count moved less than 2%. A value that cannot be derived safely is &#x60;null&#x60; with a &#x60;null_reason&#x60;. &#x60;periods&#x60; stays exactly as reported. | [optional] 

## Example

```python
from financial_reports_generated_client.models.companies_financials_retrieve200_response import CompaniesFinancialsRetrieve200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompaniesFinancialsRetrieve200Response from a JSON string
companies_financials_retrieve200_response_instance = CompaniesFinancialsRetrieve200Response.from_json(json)
# print the JSON string representation of the object
print(CompaniesFinancialsRetrieve200Response.to_json())

# convert the object into a dict
companies_financials_retrieve200_response_dict = companies_financials_retrieve200_response_instance.to_dict()
# create an instance of CompaniesFinancialsRetrieve200Response from a dict
companies_financials_retrieve200_response_from_dict = CompaniesFinancialsRetrieve200Response.from_dict(companies_financials_retrieve200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


