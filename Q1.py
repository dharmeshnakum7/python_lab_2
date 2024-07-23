#question 1
def interchange_first_last(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
input_list = [12, 35, 9, 56, 24]
output_list = interchange_first_last(input_list)
print(output_list)  
