def sort_employees_by_age(input_l):
    # input_1 = sorted(input_l,key=lambda x:x[1])
    # print(input_1)
    pass
    for i in range(len(input_1)-1):
        if input_1[i][1] > input_1[i+1][1]:
            
            input_1[i],input_1[i+1] = input_1[i+1],input_1[i]
    print(input_1)


input_1 = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("David", 25), ("Eve", 28)]
output_1 = sort_employees_by_age(input_1)
