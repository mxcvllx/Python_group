""""""
"""
2. Berilgan dict da city key o’rniga location bilan chiqaring
"""

sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "Newyork"}


sample_dict["location"] = sample_dict["city"]
del sample_dict["city"]
print(sample_dict)