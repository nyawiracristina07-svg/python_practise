#1
person = {"name": "Alice", "age": 30, "job": "Engineer"}
print(person["name"])
print(len(person))
print(person)

#2
prices = {"apple": 0.5, "banana": 0.25, "orange": 0.75}
prices ["banana"] = 0.3
print(prices)
prices["cherry"] = 0.1
print(prices)
add = {"pear":0.7,"kiwi":0.4}
update = prices | add 
print(update)

#3
car = {"brand": "Toyota", "model": "Camry", "year": 2020,"color": "blue"}
print (list(car))

#4
stuff =  [("square", "blue"), ("triangle", "red"), ("circle", "yellow")]
stuff_dict = dict(stuff)
print(dict(stuff)) 
stuff_dict["rectangle"] = "green"
print(stuff_dict)
del stuff_dict["circle"]
print(stuff_dict)
stuff_dict.pop("triangle")
print(stuff_dict)
print(list(tuple(stuff_dict.items())))

#5 
stock = {"pen": 12, "book": 3} 
#print (stock["ruler"]) 
#KeyError: 'ruler'
print(stock.get("ruler"))
# This will return 0, the default value set for the key "ruler"
print(stock.get("ruler", 0))