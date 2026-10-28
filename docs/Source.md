# Source


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the source. Filter filings with &#x60;?source&#x3D;&lt;id&gt;&#x60;. | [readonly] 
**name** | **str** | Generic label identifying the regional authority for this data source. Not unique: several sources can share a label, so use &#x60;id&#x60; to tell them apart. | [readonly] 
**url** | **str** | Homepage URL for the data source, when available. | [readonly] 
**description** | **str** | Description of the data source. | [readonly] 
**has_named_speakers** | **bool** | True if this source&#39;s call transcripts are confirmed to name each speaker (name, title, affiliation), false if they are confirmed to use generic labels such as &#39;Speaker 1&#39;, null if not yet measured. Treat null as unknown, not as false: an unmeasured source is not the same claim as a confirmed-generic one. Not meaningful for sources without transcripts. | [readonly] 

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


