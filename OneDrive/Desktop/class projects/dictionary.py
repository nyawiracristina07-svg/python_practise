ages = {"ada": 36, "bob": 42, "carol": 29, 0 : "ZERO VALUE", 0 : "ZERO VALUE AGAIN"}
print(ages["ada"]) 
print(len(ages))
print(ages)

print(ages[0])  # This will raise a KeyError because dictionaries are not indexed by integers
print(ages.get("bob", 0))  # This will return 42, the value associated with the key "bob"

#when you try to get it directly without usingg get and you pick the wrong value, the program will stop runnign from there,
#but if you use get then it will return the default value you set, in this case 0, and the program will continue running

age = {"ada": 36,}
print ( "Ada" in age)
print(36 in age)


stock = {"apple" : 5}
stock["pear"] = 3
print(stock)
stock.update({"pear":6,"fig":4})
print(stock)
del stock ["pear"]
n = stock.pop("apple")
print(n, stock)


prices = {"apple": 0.40, "banana": 0.50, "orange": 0.60}
print(list(prices.keys()))
print(list(prices.values()))
print(list(prices.items())) 
print(sum(prices.values()))  # This will return the sum of all the values in the dictionary

#merging dics

defaults = {"theme": "light", "language": 12}
user = {"language" :14}
settings = defaults | user
print(settings)  # This will print {'theme': 'light', 'language': 14}, with the value from user overriding the default
defaults |= {"language": 14}
print(defaults)  # This will print {'theme': 'light', 'language': 14}, with the value from user overriding the default

#nested data

students = {
    "name": "Alice",
    "grades": [90, 85, 92],
    "address": {
        "street": "123 Main St" },
}

print(students["grades"][1])  # This will print 85, the second grade in the list
print(students["address"]["street"])  # This will print "123 Main St", the street in the nested dictionary
print(len(students["grades"]))  # This will print 3, the number of grades in the list

# sorted == arranges them in alphabetic order 