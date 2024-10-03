first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) > 5 ]
second_result =[(x,y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result ={**{x:len(x) for x in first_strings  if len(x) % 2 == 0}, # ** распаковывает словарь и объеденяет их в один по очереди согласно тому как написан код.
               **{y: len(y) for y in second_strings if len(y) % 2 == 0}}
print(first_result)
print(second_result)
print(third_result)
