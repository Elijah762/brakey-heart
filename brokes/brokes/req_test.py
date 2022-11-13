import requests

url = 'http://127.0.0.1:8000/api/v1/send/'

data = {
    "x_acc": 2.01,
    "y_acc": 3.01,
    "z_acc": 4.01,
}

x = requests.post(url, json=data)
print(x.text)
