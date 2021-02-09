import requests
import json
import sys

jsonData_A = requests.get("https://static.cookpad.com/hr/screen/category-1.json").json()
jsonData_B = requests.get("https://static.cookpad.com/hr/screen/category-2.json").json()

def hasKey(arrayA, key):
    for dic in arrayA:
        if dic["name"] == key:
            return True
    return False

def recursion(arrayA, arrayB):
    for x in range(len(arrayA)):
        for y in range(len(arrayB)):
            if not hasKey(arrayA, arrayB[y]["name"]):
                arrayA.append({"name": arrayB[y]["name"]})
        if "subcategories" in arrayA[x] and \
            "subcategories" in arrayB[x]:
            recursion(arrayA[x]["subcategories"],arrayB[x]["subcategories"])

if jsonData_A["name"] == jsonData_B["name"]:
    recursion(jsonData_A["subcategories"],jsonData_B["subcategories"])
else:
    print([jsonData_A,jsonData_B])