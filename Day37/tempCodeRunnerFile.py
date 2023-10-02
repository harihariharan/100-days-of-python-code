
response = requests.post(url=pixel_posting_endpoint, json=pixel_config, headers=headers)
print(response.text)