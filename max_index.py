def max_index(list_numbers):
    if not list_numbers:
        return None
    else:
        return list_numbers.index(max(list_numbers))

list_numbers= (40, 50, 10, 90, 100, 70)
result =(max_index(list_numbers))
print(result)