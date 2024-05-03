def table(n):
    #a variable to store the degree since we will be manipulating it
    exp = (2**n)//2
    print(exp)
    # Instantiate an empty table to start the multi-dimensional list
    global table
    table = []
    #loop through the array and create an empty array so that it becomes multi-dimensional
    for _ in range(2**n):
        table.append([])
        print(table)

    #Populate the array for the different combinations 
        #Logic: We will use the for loop with a step which will step starting from 2**n/2 times and continuously divided by 2 until the resultt is 1, after each step the alternating variable will change from 0 to 1
        #After we will populate the spaces with the last element of the stop 
        #Loop n times to represent a cloumn for every variable
        for x in range(n):
            #Create a variable that will alternate between 0 and 1
            first_index = 0
            start = 0
            #print(len(table))
            for i in range (0,len(table),exp):
                table[i].append(start)                
                if i != 0:
                    for y in range(first_index,i):
                        table[y]=start
                    if (i + exp) > len(table)-1:
                        for z in range(i,len(table)):
                            table[z] = 1
                if start == 0:
                    start =1
                else:
                    start = 0
                first_index = i
            exp = exp//2
        print(table)
        
table(4)

