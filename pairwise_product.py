def pairwise_product(list_1, list_2):
    l=[]
    if len(list_1) != len(list_2):
        raise ValueError("Kindly input again as lists must have the same length")

    else:
        for x, y in zip(list_1, list_2):
             product = x * y
             l.append(product)
            
    return l

list_1 = [40, 50, 10, 90]
list_2 = [6, 2, 2, 5]
result = pairwise_product(list_1, list_2)
print(result)