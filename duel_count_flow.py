from prefect import flow, task
from prefect.task_runners import ConcurrentTaskRunner

@task
def count_one():
    for i in range(1,1000000):
        print(i)
    return 42

@task
def count_two():
    for i in range(-1000000,0):
        print(i)
    return 43

@flow(task_runner=ConcurrentTaskRunner)
def duel_count():
    ans1 = count_one()
    ans2 = count_two()
    return

from prefect.flow_runners import SubprocessFlowRunner
from prefect.deployments import DeploymentSpec

DeploymentSpec(
    flow_location="duel_count_flow.py",
    name="duel-count-deployment",
    flow_runner=SubprocessFlowRunner(),
)