# AgentKeyClaimRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_token** | **str** | The &#x60;claim_token&#x60; returned in the signup 409 response. | 

## Example

```python
from financial_reports_generated_client.models.agent_key_claim_request import AgentKeyClaimRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentKeyClaimRequest from a JSON string
agent_key_claim_request_instance = AgentKeyClaimRequest.from_json(json)
# print the JSON string representation of the object
print(AgentKeyClaimRequest.to_json())

# convert the object into a dict
agent_key_claim_request_dict = agent_key_claim_request_instance.to_dict()
# create an instance of AgentKeyClaimRequest from a dict
agent_key_claim_request_from_dict = AgentKeyClaimRequest.from_dict(agent_key_claim_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


