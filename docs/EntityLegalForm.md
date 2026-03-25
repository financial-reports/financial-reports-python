# EntityLegalForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elf_code** | **str** | The 4-character ISO 20275 ELF code (e.g., XJHM). | [readonly] 
**name** | **str** | Human-readable name of the legal form. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.entity_legal_form import EntityLegalForm

# TODO update the JSON string below
json = "{}"
# create an instance of EntityLegalForm from a JSON string
entity_legal_form_instance = EntityLegalForm.from_json(json)
# print the JSON string representation of the object
print(EntityLegalForm.to_json())

# convert the object into a dict
entity_legal_form_dict = entity_legal_form_instance.to_dict()
# create an instance of EntityLegalForm from a dict
entity_legal_form_from_dict = EntityLegalForm.from_dict(entity_legal_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


