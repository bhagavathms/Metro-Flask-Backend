import requests

#for Getting the Request form extenal source
source=input("from=")
destination=input("to=")
BASE="http://127.0.0.1:5000/"
response=requests.get(BASE+"route?from="+source+"&to="+destiantion"/")
print(response.json())