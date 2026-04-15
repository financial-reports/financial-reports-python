# CompanyFinancialStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fiscal_year** | **int** |  | 
**fiscal_period** | **str** |  | 
**period_start_date** | **date** |  | 
**period_end_date** | **date** |  | 
**statement_type** | **str** |  | 
**statement_type_display** | **str** |  | 
**currency** | [**CurrencyCompact**](CurrencyCompact.md) |  | 
**source_filing_id** | **int** |  | 
**source_filing_release_date** | **datetime** |  | 
**line_items** | [**List[FinancialLineItemCompact]**](FinancialLineItemCompact.md) |  | [readonly] 

## Example

```python
from financial_reports_generated_client.models.company_financial_statement import CompanyFinancialStatement

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyFinancialStatement from a JSON string
company_financial_statement_instance = CompanyFinancialStatement.from_json(json)
# print the JSON string representation of the object
print(CompanyFinancialStatement.to_json())

# convert the object into a dict
company_financial_statement_dict = company_financial_statement_instance.to_dict()
# create an instance of CompanyFinancialStatement from a dict
company_financial_statement_from_dict = CompanyFinancialStatement.from_dict(company_financial_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


