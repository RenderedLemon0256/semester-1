
def func_1(lst_value): 
    ''' 
    gets the average of the values of the list inputted
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value 