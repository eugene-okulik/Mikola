my_dict = {
    "tuple": (False, "string", 1, 3.14, None),
    "set": {3.14, 10, 5, None, 7},
    "list": ["hello", "world", "python", bool, None],
    "dict": {
        "list": [1, 2, 3],
        "tuple": (False, True),
        "set": {4, 5, 8},
        "string": "Hello my world!!!",
        77: bool,
    },
}

#  tuple
print(my_dict["tuple"][-1])
#  list
my_dict["list"].append(True)
print(my_dict["list"])
my_dict["list"].pop(1)
print(my_dict["list"])
# dict
my_dict["dict"][("i am a tuple",)] = (
    1,
    5,
)
print(my_dict["dict"])
my_dict["dict"]["list"].pop(2)
print(my_dict["dict"]["list"])
# set
my_dict["set"].add(False)
print(my_dict["set"])
my_dict["set"].remove(3.14)
print(my_dict["set"])
print(my_dict)
