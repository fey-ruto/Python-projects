def OddEvenCount(int_list):
    odd_count = 0
    even_count = 0

    for num in int_list:
        if num % 2 == 0:  
            even_count += 1
        else:
            odd_count += 1

    count_dict = {'odd': odd_count, 'even': even_count}

    return count_dict

int_list = int(input("Kindly enter a list of integers:"))
print(OddEvenCount(int_list))
  
