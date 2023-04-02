#pip install reguests
import requests
import json

response = requests.get ("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
# print(response.text)
print(type(todos))
print (todos)