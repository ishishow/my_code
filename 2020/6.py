import requests
import json
import sys

url = "https://static.cookpad.com/hr/screen/categories.json"
response = requests.get(url)
jsonData = response.json()


args = sys.argv
if len(args) != 2:
    print("Error please input recipe name! \n if you want to look all recipes, you should input [all] !")
    sys.exit()

recipe_name = args[1]

class Recipe:
    count = 0
    name = ""
    def __init__(self, name):
        self.count = 0
        self.name = name

    def down(self, arrays, flag):
        for array in arrays:
            if array["name"] == self.name:
                flag = True
            if "recipes" in array:
                if flag:
                    self.count += array["recipes"]
            if "subcategories" in array:
                self.down(array["subcategories"],flag)
        return self.count

recipe = Recipe(recipe_name)
if recipe_name == "all":
    print(recipe.down(jsonData["subcategories"],True))
else:
    print(recipe.down(jsonData["subcategories"],False))

