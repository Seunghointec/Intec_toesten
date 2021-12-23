group_of_people = ['Alex', 'Eliot', 'Veronica', 'Lucy', 'Wouter', 'Bart']

print([x[0]
       for x in group_of_people
       ])

numbers = list(range(100))

sum_numbers = sum(numbers)

print(sum_numbers)

#3b

GDPs = [('Germany', 3_863.344), ('United Kingdom',2_743.586),
       ('France', 2_707.074), ('Italy', 2_001.440)]

list_GDP = list(filter(lambda GDP: GDP[1], GDPs))
print(list_GDP)

#personally I find this more easy, less wording
for i in GDPs:
    print(i)

#3c
#create a list of lists
matrix = [[x for x in range(10)] for y in range(10)]
print(matrix)
