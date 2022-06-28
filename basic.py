import requests
from prefect import flow

@flow
def basic_func():
    print("Something done here...")
    return 152

basic_func()

@flow
def basic_api_call(url):
    return requests.get(url).json()

state = basic_api_call('https://api.github.com')
print(state.result())