# CompanySuccessionLink

Inline schema type for `predecessors` / `successors` on CompanySerializer (#1926).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal id of the linked company. | 
**name** | **str** | Name of the linked company. | 
**kind** | [**KindEnum**](KindEnum.md) | How the issuer changed: reorganization (holding company, share exchange, redomicile), spin_off, merger or other.  * &#x60;reorganization&#x60; - Reorganization * &#x60;spin_off&#x60; - Spin-off * &#x60;merger&#x60; - Merger * &#x60;other&#x60; - Other | 
**effective_date** | **date** | Date the successor took over as issuer, when known. | 

## Example

```python
from financial_reports_generated_client.models.company_succession_link import CompanySuccessionLink

# TODO update the JSON string below
json = "{}"
# create an instance of CompanySuccessionLink from a JSON string
company_succession_link_instance = CompanySuccessionLink.from_json(json)
# print the JSON string representation of the object
print(CompanySuccessionLink.to_json())

# convert the object into a dict
company_succession_link_dict = company_succession_link_instance.to_dict()
# create an instance of CompanySuccessionLink from a dict
company_succession_link_from_dict = CompanySuccessionLink.from_dict(company_succession_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


