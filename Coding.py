import requests

myobj = {
      "id": 1,
      "name": "NEWserver1",
      "IP": "192.168.1.100",
      "Desc": "dns server"
	  }

p = {'id': 2}

change = { 'name' : 'NEW SERVER'}

try:
	inventory = requests.get("https://my-json-server.typicode.com/codbegin/clneaxes/servers", params = p)
	# inventory = requests.get("https://my-json-server.typicode.com/BiancaSozzi/catalogoAngular/products", params = p)

	print(inventory.text)
	print("------------- ")
	x = requests.post("https://my-json-server.typicode.com/codbegin/clneaxes/servers", data = change)
	print(x.text)
	# y = requests.get("https://my-json-server.typicode.com/BiancaSozzi/catalogoAngular/products")
	# print(y.text)

except:
	print("error")


# https://my-json-server.typicode.com/BiancaSozzi/catalogoAngular/db

# inventory = requests.get("https://my-json-server.typicode.com/codbegin/clneaxes/db")
# inventory = requests.get("https://octane.klarna.net/api/systems")


# if inventory.status_code == 200:
# 	print(inventory.json)
# 	print(inventory.text)
# else:
# 	print("error")


