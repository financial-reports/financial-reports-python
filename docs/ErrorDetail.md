# ErrorDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | A human-readable message describing the error. | 
**type** | **str** | Machine-readable error code, e.g. &#x60;authentication_required&#x60;. Present on some errors only. | [optional] 
**resolution** | **str** | A human-readable hint on how to fix the request. Present on some errors only. | [optional] 
**error_type** | **str** | Machine-readable error code on validation errors. Present on some errors only. | [optional] 

## Example

```python
from financial_reports_generated_client.models.error_detail import ErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetail from a JSON string
error_detail_instance = ErrorDetail.from_json(json)
# print the JSON string representation of the object
print(ErrorDetail.to_json())

# convert the object into a dict
error_detail_dict = error_detail_instance.to_dict()
# create an instance of ErrorDetail from a dict
error_detail_from_dict = ErrorDetail.from_dict(error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


