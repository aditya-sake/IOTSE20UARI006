import requests
url = "http://localhost:8885/api/messages"
#server initiated from this port number. 5000
data = {
"message": "Aditya Sake"
}
response  = requests.post(url,json=data)
print(response.text)

#message request
receive_url = url = "http://localhost:8885/api/send"
response = requests.get(receive_url)
print("Server Side:",response.json().get("message","No message"))
