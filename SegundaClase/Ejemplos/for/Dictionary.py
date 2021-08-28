dict1 = {
    "model": "mustang",
    "year": 1964,
    "producer": "ford"
}

print("Las llaves son")
for key in dict1.keys():
    print(key)

print("Los valores son")
for value in dict1.values():
    print(value)

print("Las llaves y valores son")
for key,value in dict1.items():
    print(key,value)