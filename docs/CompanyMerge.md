# CompanyMerge

One merge of a duplicate company into its canonical company. The ids stay set even if either company is later deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**shell_id** | **int** | Id of the retired duplicate. Stop using this id; it will not appear in the company list. | [readonly] 
**canonical_id** | **int** | Id of the surviving canonical company. Repoint references here. | [readonly] 
**shell_name** | **str** |  | [optional] 
**canonical_name** | **str** |  | [optional] 
**pattern** | **str** | Why the pair matched, e.g. exact_duplicate, suffix_variant, gb_us_adr. | [readonly] 
**confidence** | **float** | Matching confidence from 0 to 1, or null for a merge made by hand. | [readonly] 
**merged_at** | **datetime** | When the merge was applied (ISO 8601, UTC). Never changes. | [readonly] 
**reversed_at** | **datetime** | Set when a merge was undone: the shell is live again and the canonical pointer no longer holds. Null for an active merge. | [readonly] 
**updated_at** | **datetime** | When this record last changed, by a merge or a reversal. Poll &#x60;updated_at_from&#x60; to receive reversals; &#x60;merged_at&#x60; alone cannot surface them because a reversal edits the existing record in place. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.company_merge import CompanyMerge

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyMerge from a JSON string
company_merge_instance = CompanyMerge.from_json(json)
# print the JSON string representation of the object
print(CompanyMerge.to_json())

# convert the object into a dict
company_merge_dict = company_merge_instance.to_dict()
# create an instance of CompanyMerge from a dict
company_merge_from_dict = CompanyMerge.from_dict(company_merge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


