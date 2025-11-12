# JobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly] 
**status** | [**StatusEnum**](StatusEnum.md) |  | [optional] 
**result_file_url** | **str** |  | [readonly] 
**error_message** | **str** |  | [optional] 
**record_count** | **int** |  | [optional] 
**records_processed** | **int** | Number of records processed so far. | [optional] 
**estimated_completion_time** | **datetime** |  | [optional] 

## Example

```python
from financial_reports_generated_client.models.job_status import JobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatus from a JSON string
job_status_instance = JobStatus.from_json(json)
# print the JSON string representation of the object
print(JobStatus.to_json())

# convert the object into a dict
job_status_dict = job_status_instance.to_dict()
# create an instance of JobStatus from a dict
job_status_from_dict = JobStatus.from_dict(job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


