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