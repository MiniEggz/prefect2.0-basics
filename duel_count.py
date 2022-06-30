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
def async_flow():
    ans1 = count_one()
    ans2 = count_two()
    return

def main():
    async_flow()

if __name__ == "__main__":
    main()

# when run can see that they are running together
# blocks of +ve and -ve counts...