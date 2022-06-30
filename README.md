# Prefect 2.0

### Sections
* [Setting up Prefect 2.0 locally](#local-setup)
* [Setting up Prefect 2.0 cloud](#cloud-setup)

<br>

# <a name="local-setup"></a>  Setting up Prefect 2.0 locally and running basic scripts

## Setting up virtual environment (using virtualenv)
Conda and venv are also compatible with Prefect 2.0.

<br>

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

<br>

## Installing Prefect 2.0
To install the latest version of 2.0:
```
$ pip install -U "prefect>=2.0b"
```
Check installation with
```
$ prefect version
```

<br>

## Installing requests for use in starter scripts

```
pip install requests
```

<br>

## Basic example of using flows in Prefect 2.0

The first is just an example of a simple flow interacting with the GitHub API.

<br>

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

if __name__ == "__main__":
    state = basic_api_call('https://api.github.com')
    print(state.result())
```

To run this as a script, simply:

```
$ python3 flow_example.py
```

<br>

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

if __name__ == "__main__":
    api_flow('https://api.github.com')
```

Run with:

```
$ python3 tasks_example.py
```

<br>

## Looking at running tasks asychronously

Prefect 2.0 uses task runners that can run sequentially or concurrently. To illustrate this, this example shows two counts (one negative and one positive) to show that both tasks are being carried out at the same time.

<br>

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

if __name__ == "__main__":
    async_flow()
```

Run the flow with:

```
$ python3 duel_count.py
```

<br>

# <a name="cloud-setup"></a> Getting started with Prefect cloud 2.0
Setting up Prefect 2.0 cloud is just a continuation of having it set up locally.

## Set up account
Go to [beta.prefect.io](https://beta.prefect.io) and set up Prefect 2.0 account (separate from Prefect 1.0). After doing this, you should be prompted to set up a workspace.

<br>

## Generate API key
Generate an API key by going to [beta.prefect.io/profile/api-keys](beta.prefect.io/profile/api-keys), add an API key, name it, set an expiration date and then save it.

<br>

## Creating and using prefect profiles
Prefect profiles are good to switch between local work and work using Prefect cloud, or between different workspaces on the cloud. To set up profiles up using:

```
$ prefect profile create {profile-name}
```

To change profile, use:

```
$ prefect profile use {profile-name}
```

All profiles are stored in /Users/{user-name}/.prefect/profiles.toml. To list them, simply:

```
$ cat ~/.prefect/profiles.toml
```

<br>

## Configuring prefect profiles
To configure the API key, activate the correct prefect profile and then:

```
$ prefect config set PREFECT_API_KEY=XXXX
```

Add the PREFECT_API_URL to the profile:

```
$ prefect cloud workspace set --workspace "{email-without-special-characters}/{workspace-slug}"
```

This command can also be found by going into your workspace at [beta.prefect.io](https://beta.prefect.io) and going to 'Workspace Settings'.

<br>

To check that everything has worked correctly, inspect the current profile:

```
$ prefect profile inspect {profile-name}
```

<br>

## Run something
Now just run any script using prefect and that history will be logged on Prefect cloud.

```
$ python3 duel_count.py
```