def min_index(list_numbers):
    if not list_numbers:
        return None
    else:
        return list_numbers.index(min(list_numbers))
    
list_numbers= (40, 50, 10, 90, 100, 70)
result =(min_index(list_numbers))
print(result)


def max_index(list_numbers):
    if not list_numbers:
        return None
    else:
        return list_numbers.index(max(list_numbers))

list_numbers= (40, 50, 10, 90, 100, 70)
result =(max_index(list_numbers))
print(result)


def smaller_indices(list_1, list_2):
    l=[]
    
    if len(list_1) != len(list_2):
        raise ValueError("Kindly input again as lists must have the same length")

    else:
        for i in range(len(list_1)):
            if list_1[i] < list_2[i]:
                
                l.append(i)        
    return l

list_1 = [40, 50, 10, 90, 100, 70]
list_2 = [60, 20, 19, 95, 30, 20]
result = smaller_indices(list_1, list_2)
print(result)

def pairwise_product(list_1, list_2):
    l=[]
    if len(list_1) != len(list_2):
        raise ValueError("Kindly input again as lists must have the same length")

    else:
        for x, y in zip(list_1, list_2):
             product = x * y
             l.append(product)
            
    return l

list1 = [40, 50, 10, 90]
list2 = [6, 2, 2, 5]
result = pairwise_product(list_1, list_2)
print(result)

