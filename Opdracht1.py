from random import randint, choice

actually_sick = choice([True, False])
kinda_sick = choice([True, False])
dont_feel_like_it = choice([True, False])

calling_in_sick = choice([True, False])

sick_days = randint(0, 10)

while 0<sick_days < 10:
    if actually_sick:
        print(f'Am I allowed to call in sick? : {calling_in_sick}')
    elif dont_feel_like_it and kinda_sick:
        print(f'Am I allowed to call in sick? : {calling_in_sick}')
        sick_days -= sick_days
else:
    if sick_days< 0:
        print(f'Am I allowed to call in sick? : {False}')

