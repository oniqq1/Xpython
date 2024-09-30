












#    exercise 2

# 1 foot = 12 inch
# 1 foot = 0,3 yard
# 1 foot = 0,000189393939 mile

def calcualateFoots(foots, CI):

    if CI not in values.keys():
        return print('Not value in database')

    if values.get(CI) * foots >= 2:
        return print(f'{foots} foots = {values.get(CI) * foots} {CI}s  \n \n')

    return print(f'{foots} foots = {values.get(CI) * foots} {CI}  \n \n')


values = {
    "inch": 12,
    "yard": 0.3,
    "mile": 0.000189393939
}

while True:

    while True:
        try:
            foots = int(input('Count foots > '))
            break
        except ValueError:
            print("Input number , not str")

    CI = input('inch , yard or mile ( "q" for quit ) > ')
    if CI == 'q': break

    calcualateFoots(foots, CI)
