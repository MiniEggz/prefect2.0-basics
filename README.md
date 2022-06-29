# Prefect 2.0
  
## Setting up Prefect 2.0 locally and running basic scripts

### Start by getting virutal environment set up (conda, venv and virtualenv seem like the best choices when using Prefect):
Create folder with clean copy of python:
```
$ virtualenv ./{dir_name}
```
cd into project directory:
```
$ cd {dir_name}
```
Activate the environment:
```
$ source ./bin/activate
```

## Installing Prefect 2.0
To install the latest version of 2.0:
```
$ pip install -U "prefect>=2.0b"
```
Check installation with
```
$ prefect version
```

## Installing requests for use in tests
```
pip install requests
```

## Basic example of using flows in Prefect 2.0

The first is just an example of a simple flow interacting with the GitHub API.
\
Create a python file, for example:

```
$ touch flow_example.py
```

and paste in this code:

```
import requests
from prefect import flow

@flow
def basic_api_call(url):
    return requests.get(url).json()

state = basic_api_call('https://api.github.com')
print(state.result())
```

To run this as a script, simply:

```
$ python3 flow_example.py
```

## Looking at using tasks within flows

This example is very similar to the previous one. It just adds an extra layer - pulling all the keys from the API response. This allows for two separate tasks.

Create new file:

```
$ touch tasks_example.py
```

Paste in the following code:

```
import requests
from prefect import flow, task

@task
def call_api(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()

@task
def print_keys(response):
    keys = []
    for key in response:
        keys.append(key)
    print(keys)
    return

@flow
def api_flow(url):
    json = call_api(url)
    print_keys(json)

api_flow('https://api.github.com')
```

Again, run with:

```
$ python3 tasks_example.py
```

## Looking at running tasks asychronously

Prefect 2.0 uses task runners that can run sequentially or concurrently. To illustrate this, this example shows two counts (one negative and one positive) to show that both tasks are being carried out at the same time.
\
Create a python file:

```
$ touch duel_count.py
```

Paste the following code in:

```
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

async_flow()
```

Run the flow with:

```
$ python3 duel_count.py
```
