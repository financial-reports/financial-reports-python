# Source


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Generic label identifying the regional authority for this data source. | [readonly] 
**url** | **str** | Homepage URL for the data source, when available. | [readonly] 
**description** | **str** | Description of the data source. | [readonly] 
**has_named_speakers** | **bool** | Tri-state: true if this source&#39;s CT (call transcript) filings are confirmed to carry named speaker attribution (name/title/affiliation), false if confirmed generic labels like &#39;Speaker 1&#39;, null if not yet measured. Treat null as &#39;not a positive match&#39;, not as false — an unmeasured source is not the same claim as a confirmed-generic one. Not meaningful for non-transcript sources. | [readonly] 

## Example

```python
from financial_reports_generated_client.models.source import Source

# TODO update the JSON string below
json = "{}"
# create an instance of Source from a JSON string
source_instance = Source.from_json(json)
# print the JSON string representation of the object
print(Source.to_json())

# convert the object into a dict
source_dict = source_instance.to_dict()
# create an instance of Source from a dict
source_from_dict = Source.from_dict(source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


