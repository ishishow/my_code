import urllib
import urllib.request
import requests
import json
import sys

save_dir = args[0]

jsonData_A = requests.get(
    "https://static.cookpad.com/hr/screen/files/index.json").json()

for i in range(0, len(jsonData_A)):
    try:
        data = urllib.request.urlopen(jsonData_A[i]).read()
        with open(save_dir + "data_"+str(i), mode="wb") as f:
            f.write(data)
    except:
        print(jsonData_A[i], "not data found")
        pass
