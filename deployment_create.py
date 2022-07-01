from prefect.flow_runners import SubprocessFlowRunner
from prefect.deployments import DeploymentSpec

DeploymentSpec(
    flow_location="basic.py",
    flow_name="basic-api-call",
    parameters={"url":"https://api.github.com"},
    name="basic-deployment",
    flow_runner=SubprocessFlowRunner(),
)

DeploymentSpec(
    flow_location="basic.py",
    flow_name="basic-func",
    name="basic-func-deployment",
    flow_runner=SubprocessFlowRunner(),
)