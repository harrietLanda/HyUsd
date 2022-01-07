import json

with open (r"Z:\USD\USD_ALab_0730\entity\books_encyclopedias01\modelling\books_encyclopedias01_modelling.usda", "r") as myfile:
    data=myfile.readlines()
    data_json = json.dumps(data, indent=4, sort_keys=True)
print(data_json)