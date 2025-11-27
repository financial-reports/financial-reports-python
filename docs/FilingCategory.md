# FilingCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Name of the disclosure category. | [readonly] 
**sort_order** | **int** | Order priority for display. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.filing_category import FilingCategory

# TODO update the JSON string below
json = "{}"
# create an instance of FilingCategory from a JSON string
filing_category_instance = FilingCategory.from_json(json)
# print the JSON string representation of the object
print(FilingCategory.to_json())

# convert the object into a dict
filing_category_dict = filing_category_instance.to_dict()
# create an instance of FilingCategory from a dict
filing_category_from_dict = FilingCategory.from_dict(filing_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


