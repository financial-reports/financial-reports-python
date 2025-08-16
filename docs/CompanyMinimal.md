# CompanyMinimal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the company. | [readonly] 
**name** | **str** | Company name. | [readonly] 
**isins** | **List[str]** | List of International Securities Identification Numbers (ISINs) associated with the company. | [readonly] 
**lei** | **str** | Legal Entity Identifier (ISO 17442). | [readonly] 
**sub_industry_code** | **str** | ISIC classification code classifying the company. | [readonly] 
**country_code** | **str** | ISO 3166-1 alpha-2 country code of the company&#39;s primary registration or headquarters. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.company_minimal import CompanyMinimal

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyMinimal from a JSON string
company_minimal_instance = CompanyMinimal.from_json(json)
# print the JSON string representation of the object
print(CompanyMinimal.to_json())

# convert the object into a dict
company_minimal_dict = company_minimal_instance.to_dict()
# create an instance of CompanyMinimal from a dict
company_minimal_from_dict = CompanyMinimal.from_dict(company_minimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


