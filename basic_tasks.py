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

def main():
    state = api_flow('https://api.github.com')

if __name__ == "__main__":
    main()