import requests


def get_api_data(url):
    json = requests.get(url)
    if json.status_code == 200:
        return json.json()
    else:
        return "false"

data = get_api_data("https://jsonplaceholder.typicode.com/todos/1")
print(data)
#>>> {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
data = get_api_data("https://jsonplaceholder.typicode.com/nedala/nedala")
print(data)
#>>> False