import requests
from prefect import flow

@flow
def basic_func():
    print("Something done here...")
    return 152

@flow
def basic_api_call(url):
    return requests.get(url).json()

def main():
    basic_func()
    state = basic_api_call('https://api.github.com')
    print(state.result())

if __name__ == "__main__":
    main()