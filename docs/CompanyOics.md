# CompanyOics

A company's label under the Open Industry Classification Standard (OICS): its primary class with the class's sector, industry group and industry, its entity type and up to two secondary classes. Public preview, OICS v0.3.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Primary class code: the class&#39;s place in the tree, SECTOR.GROUP.INDUSTRY.CLASS (e.g. &#x60;TC.SC.SEM.CHP&#x60;). Null for an entity type that carries no class. | 
**name** | **str** | Primary class name. Null when &#x60;code&#x60; is. | 
**sector** | [**OicsNodeRef**](OicsNodeRef.md) | The class&#39;s sector. Null when &#x60;code&#x60; is. | 
**group** | [**OicsNodeRef**](OicsNodeRef.md) | The class&#39;s industry group. Null when &#x60;code&#x60; is. | 
**industry** | [**OicsNodeRef**](OicsNodeRef.md) | The class&#39;s industry. Null when &#x60;code&#x60; is. | 
**entity_type** | **str** | What kind of entity the company is, decided before its activity: OPERATING, HOLDING, FUND, SPAC_SHELL, FINANCING_VEHICLE or PUBLIC_SECTOR. FUND, SPAC_SHELL, FINANCING_VEHICLE and PUBLIC_SECTOR carry no class; a HOLDING carries one only when most of its value sits in one business. | 
**secondaries** | [**List[OicsNodeRef]**](OicsNodeRef.md) | Up to two further classes the company has a material business in. Never the primary. | 
**basis** | **str** | What the label rests on: &#x60;revenue&#x60; (reported revenue by segment or product), &#x60;nav&#x60; (a holding&#39;s net asset value), &#x60;filings&#x60; (other figures from the company&#39;s filings) or &#x60;description&#x60; (the company&#39;s description). | 
**taxonomy_version** | **str** | OICS version the label was decided under, e.g. &#x60;0.3&#x60;. | 
**classified_at** | **datetime** | When the label was last written (ISO 8601, UTC). | 
**contested** | **bool** | True when an independent second reading disagreed with the label: of the company&#39;s description, for a label with basis &#x60;description&#x60;, or a second mapping of its revenue lines, for a label decided on reported revenue. The label stands; &#x60;alternate&#x60; is the other reading. A label decided on other figures from the company&#39;s filings is never contested. | 
**alternate** | [**OicsNodeRef**](OicsNodeRef.md) | The other reading of a contested label: a class, or an entity type (&#x60;code&#x60; is then e.g. &#x60;HOLDING&#x60;). Information only: it is not a second classification and no filter matches it. Null when the label is not contested. | 

## Example

```python
from financial_reports_generated_client.models.company_oics import CompanyOics

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyOics from a JSON string
company_oics_instance = CompanyOics.from_json(json)
# print the JSON string representation of the object
print(CompanyOics.to_json())

# convert the object into a dict
company_oics_dict = company_oics_instance.to_dict()
# create an instance of CompanyOics from a dict
company_oics_from_dict = CompanyOics.from_dict(company_oics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


