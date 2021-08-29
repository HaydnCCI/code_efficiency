
dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'orange': 4, 'banana': 8}

combined_dict = {**dict_1, **dict_2}

print(combined_dict)
# Output
# {'apple': 9, 'banana': 8, 'orange': 4}
