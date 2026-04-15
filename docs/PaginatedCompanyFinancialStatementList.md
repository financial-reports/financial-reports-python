# PaginatedCompanyFinancialStatementList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[CompanyFinancialStatement]**](CompanyFinancialStatement.md) |  | 

## Example

```python
from financial_reports_generated_client.models.paginated_company_financial_statement_list import PaginatedCompanyFinancialStatementList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCompanyFinancialStatementList from a JSON string
paginated_company_financial_statement_list_instance = PaginatedCompanyFinancialStatementList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCompanyFinancialStatementList.to_json())

# convert the object into a dict
paginated_company_financial_statement_list_dict = paginated_company_financial_statement_list_instance.to_dict()
# create an instance of PaginatedCompanyFinancialStatementList from a dict
paginated_company_financial_statement_list_from_dict = PaginatedCompanyFinancialStatementList.from_dict(paginated_company_financial_statement_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


