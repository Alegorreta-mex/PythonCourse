"""Se pueden crear dictionarios con {} o el contructor dict"""

dict1 = {
    "model": "mustang",
    "year": 1964,
    "producer": "ford"
}
dict2 = dict((("model", "mustang"), ("year", 1964), ("producer", "ford")))

if dict1 == dict2:
    print("el dict 1 {} es igual a el dict 2 {}".format(dict1, dict2))

"""Los dictionarios trabajan con keys"""

dict1["color"] = "Red"
print("El nuevo dict es {}".format(dict1))
dict1["color"] = "blue"
print("El nuevo dict es {}".format(dict1))
dict1.pop("year")
print("El nuevo dict es {}".format(dict1))

"""Los dictionarios pueden estar aninados"""
dict3 = {
    "model": "mustang",
    "year": 1964,
    "producer": "ford",
    "details": {
        "color": "red",
        "doors": 2
    }
}
print("El nuevo dict es {}".format(dict3))
