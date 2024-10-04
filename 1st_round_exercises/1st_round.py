import time





# exercise 1

# time in world where work this washing machine
time_working = 0

# little database with mode of work washing machine
work_mode = {
    'cotton': [1000, 90, 40],  # first num = count turn (отжим), second num = temperature , third = time (minute)
    'speed': [600, 40, 20],
    'synthetics': [1000, 60, 60],
    'slow': [0, 30, 90]
}

washing_machines = {
    'work': (' ___________________\n'
             '|  x       -  - O   |\n'
             ' -------------------\n'
             '|       ______      |\n'
             '|     (        )    |\n'  # washing machine work?????
             '|    (__________)   |\n'
             '|     (********)    |\n'
             '|      ---------    |\n'
             '|                   |\n'
             ' -------------------\n'),
    'off': (' ___________________\n'
            '|  x       -  - O   |\n'
            ' -------------------\n'
            '|       ______      |\n'
            '|     (        )    |\n'  # washing machine off ?????
            '|    (          )   |\n'
            '|     (        )    |\n'
            '|      ---------    |\n'
            '|                   |\n'
            ' -------------------\n'),
}


def turn_on(sysInfo: list[int], mode: str):
    global time_working
    time_working += sysInfo[2]



    print(washing_machines.get('work'))
    time.sleep(sysInfo[2] / 10)
    print(
        f"The washing machine worked {sysInfo[2]} minutes in {mode} mode \n"
        f"and at {sysInfo[0]} speed , on temperature {sysInfo[1]}. The clothes were washed  \n \n \n")





while True:
    print(f'Working time = {round(time_working / 60)} hours ( about )')  # округленно

    print(washing_machines.get('off'))
    user_input = input("Write a mode to wash ('q' for quit) \n"
                       " 'cotton','speed','synthetics', 'slow' > ")

    if user_input == 'q':
        break

    if user_input in work_mode:
        turn_on(work_mode.get(user_input), user_input)
    else:
        print('Not mode \n \n')






print('\n \n \n \n')








#    exercise 2

# 1 foot = 12 inch
# 1 foot = 0,3 yard
# 1 foot = 0,000189393939 mile

# calculate count foots in another kind measurement
def calcualateFoots(foots, CI):
    if CI not in values.keys():
        return print('Not value in database')

    if values.get(CI) * foots >= 2:
        return print(f'{foots} foots = {values.get(CI) * foots} {CI}s  \n \n')

    return print(f'{foots} foots = {values.get(CI) * foots} {CI}  \n \n')


# little database with kinds measurements
values = {
    "inch": 12,
    "yard": 0.3,
    "mile": 0.000189393939
}

# main logic of calculate
while True:

    while True:
        try:
            foots = int(input('Count foots > '))
            break
        except ValueError:
            print("Input number , not str\n")

    CI = input('inch , yard or mile ( "q" for quit ) > ')
    if CI == 'q': break

    calcualateFoots(foots, CI)
