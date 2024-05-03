def min_index(list_numbers):
    if not list_numbers:
        return None
    else:
        return list_numbers.index(min(list_numbers))
    
list_numbers= (40, 50, 10, 90, 100, 70)
result =(min_index(list_numbers))
print(result)

