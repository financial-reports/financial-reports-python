# AgentSignupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The account owner&#39;s real email address. | 
**agent_name** | **str** | 1-64 chars: letters, digits, space, _ or -. | 

## Example

```python
from financial_reports_generated_client.models.agent_signup_request import AgentSignupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSignupRequest from a JSON string
agent_signup_request_instance = AgentSignupRequest.from_json(json)
# print the JSON string representation of the object
print(AgentSignupRequest.to_json())

# convert the object into a dict
agent_signup_request_dict = agent_signup_request_instance.to_dict()
# create an instance of AgentSignupRequest from a dict
agent_signup_request_from_dict = AgentSignupRequest.from_dict(agent_signup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


