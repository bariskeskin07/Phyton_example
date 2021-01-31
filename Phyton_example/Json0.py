# -*- coding: utf-8 -*-

import json

data = '{"firstName":"engin","lastName":"demiroğ"}'

y = json.loads(data)

type(y)

print(y["firstName"])
print(y["lastName"])

customer = {
        "firstName":"Engin",
        "email":"engindemirog@gmail.com"
        }
customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Engin"))