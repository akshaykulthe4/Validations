import requests
import json
import jsonpath

#for get method
url = input("Enter Your URL:- ")
#url = https://reqres.in/api/users?page=2

response = requests.get(url)

Return_Content = response.content
Expected_Content = input("Enter Your Expected Content:- ")

#Expected =


print(response)
print(response.content)
print(response.headers)

assert response.status_code == 200
assert response.content == Return_Content
Return_Content == Expected_Content