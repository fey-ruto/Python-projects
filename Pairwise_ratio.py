def pairwise_ratio(list_1, list_2):
    l=[]
    if len(list_1) != len(list_2):
        raise ValueError("Kindly input again as lists must have the same length")

    else:
        for x,y in zip(list_1,list_2):
            ratio = x / y
            l.append(ratio)
            
    return l

list_1 = [40, 50, 10, 90]
list_2 = [60, 20, 19, 95]
result = pairwise_ratio(list_1, list_2)
print(result)
    
