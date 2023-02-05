""""""
"""
3. Berilgan dict da minimum value qiymat keyi ni qaytaring
"""


sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}

minn = min(sample_dict, key=sample_dict.get)
print(minn)