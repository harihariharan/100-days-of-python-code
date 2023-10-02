import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "harihariharanj"
USERNAME = "hariharanj"

user_params = {
    "token" : "harihariharanj",
    "username" : "hariharanj",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : "graph1",
    "name" : "Coding Graph",
    "unit" : "time",
    "type" : "float",
    "color" : "ajisai"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

GRAPH_ID  = "graph1"
today = datetime.now()

pixel_posting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "5"
}

# response = requests.post(url=pixel_posting_endpoint, json=pixel_config, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230906"
pixel_update_config = {
    "quantity" : "3.5"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230906"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)