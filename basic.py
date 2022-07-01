import requests
from prefect import flow

# flows
@flow
def basic_func():
    print("Something done here...")
    return 152

@flow
def basic_api_call(url):
    return requests.get(url).json()

# deployments
from prefect.flow_runners import SubprocessFlowRunner
from prefect.deployments import DeploymentSpec

DeploymentSpec(
    flow_location="basic.py",
    flow_name="basic-api-call",
    parameters={"url":"https://api.github.com"},
    name="basic-deployment",
    flow_runner=SubprocessFlowRunner(),
)

# main
def main():
    basic_func()
    state = basic_api_call('https://api.github.com')
    print(state.result())

if __name__ == "__main__":
    main()