from prefect import flow

@flow
def new_flow():
    print("test")
    return

from prefect.flow_runners import SubprocessFlowRunner
from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import IntervalSchedule
from datetime import timedelta

DeploymentSpec(
    flow_location="test.py",
    flow_name="new-flow",
    name="basic-test-deployment",
    flow_runner=SubprocessFlowRunner(),
    tags=['test1'],
    schedule=IntervalSchedule(interval=timedelta(seconds=20)),
)