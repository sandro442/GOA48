def remove_duplicates(apples):
    return list(set(apples))
apples_list = ["პანტა", "პანტა", "გორული"]
unique_apples = remove_duplicates(apples_list)
print(unique_apples)