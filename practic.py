# def by_3(x):
#     return x * 3
#
# def by_add(x):
#     return x % 2


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = map(by_3, filter(by_add, my_list))
# print(list(result))
# это долго много и не удобно
#######################################################
# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_comp_1 = [x * 2 for x in my_numbers]
# print(list_comp_1)
#  Быстро и удобно
#########################################################

# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_comp_1 = [x * 2 for x in my_numbers if x > 5]
# print(list_comp_1)

#########################################################

# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_comp_1 = [x * 3 for x in my_numbers if x % 2]
# print(list_comp_1)

########################################################

# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_comp_1 = [x * 3 if x > 2 else x * 10 for x in my_numbers]
# print(list_comp_1)

#########################################################

# my_numbers = [1, "A", 3, "f", 5, "G", 7, 8, 9]
# list_comp_1 = [x if type(x) == str else x * 10 for x in my_numbers]
# print(list_comp_1)

##########################################################

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_comp_1 = [x * y for x in my_numbers for y in my_numbers_1]
# print(list_comp_1)
#
# list_comp_1 = [x * y for x in my_numbers for y in my_numbers_1 if x % 2 == 0]
# print(list_comp_1)

list_comp_1 = [x * y for x in my_numbers for y in my_numbers_1 if x % 2 == 0 and y // 2 ]
print(list_comp_1)

############################################################################################

# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = {x for x in my_numbers }
# print(result)
#
# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = {x: x ** 2 for x in my_numbers}
# print(result)
