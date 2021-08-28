cars = [
    {
        "model": "mustang",
        "year": 1964,
        "producer": "ford"
    },
    {
        "model": "Civic",
        "year": 2016,
        "producer": "Toyota"
    },
    {
        "model": "jetta",
        "year": 2001,
        "producer": "volswagen"
    },

]

for car in cars:
    print("Carro:")
    for key, value in car.items():
        print("key: {} value:{}".format(key, value))
