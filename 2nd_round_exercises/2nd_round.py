# def temperature_degree(temp: float | int) -> str:
#     if temp <= 0:
#         return "A cold, isn't it?\n"
#     elif 0 < temp < 10:
#         return "Cool\n"
#     else:
#         return "Nice weather we're having\n"
#
#
# while True:
#     user_input = input('Введіть температуру (число)\n("q" for quit)\n > ')
#     if user_input == 'q':
#         break
#
#     try:
#         print(temperature_degree(float(user_input)))
#     except ValueError:
#         print('Введино текст , введіть число або "q" для виходу \n\n')


labyrinth = [['▇','█','█',' ','█'],
             ['█',' ',' ',' ','█'],
             [' ',' ','█',' ','█'],  #  знак $ значит найденый путь
             ['█',' ','█','█','█'],
             ['█',' ',' ',' ','█'],
             ['█','█','█','█','█']]


def print_labyrinth(labyrinth:list[list[str]]):
    for row in range(len(labyrinth)):
        print(labyrinth[row])

def do_step(count_steps:int,matrix:list[list[str]] , labyrinth:list[list[str]]) -> None:
    for row in range(len(matrix)):
        for place in range(len(matrix[row])):
            if matrix[row][place] == count_steps:
                if row > 0 and matrix[row - 1][place] == 0 and labyrinth[row - 1][place] == ' ':
                    matrix[row - 1][place] = count_steps + 1
                if place > 0 and matrix[row][place - 1] == 0 and labyrinth[row][place - 1] == 0:
                    matrix[row][place - 1] = count_steps + 1
                if place < len(matrix) - 1 and matrix[row + 1][place] == 0 and labyrinth[row + 1][place] == ' ':
                    matrix[row + 1][place] = count_steps + 1
                if place < len(matrix[row]) - 1 and matrix[row][place + 1] == 0 and labyrinth[row][place + 1] == ' ':
                    matrix[row][place + 1] = count_steps + 1
def find_exit(labyrinth:list[list[str]] , start_pos : list[int], end_pos : list[int]) -> str : # exit has been find. exit hasn't been find..
    matrix = []
    for row in range(len(labyrinth)):
        matrix.append([])
        for place in range(len(labyrinth[row])):
            matrix[-1].append(0)
    matrix[start_pos[0]][start_pos[1]] = 1

    count_step = 0
    while matrix[end_pos[0]][end_pos[1]] == 0:
        count_step += 1
        do_step(count_step,matrix,labyrinth)


    pos = matrix[end_pos[0]][end_pos[1]]
    way = [[end_pos[0], end_pos[1]]]
    while pos > 1:
        if end_pos[0] > 0 and matrix[end_pos[0] - 1][end_pos[1]] == pos - 1:
            end_pos[0] = end_pos[0]-1
            way.append([end_pos[0], end_pos[1]])
            pos -= 1
        elif end_pos[1] > 0 and matrix[end_pos[0]][end_pos[1] - 1] == pos - 1:
            end_pos[1] = end_pos[1]-1
            way.append([end_pos[0], end_pos[1]])
            pos -= 1
        elif end_pos[0] < len(matrix) - 1 and matrix[end_pos[0] + 1][end_pos[1]] == pos - 1:
            end_pos[0] = end_pos[0]+1
            way.append([end_pos[0], end_pos[1]])
            pos -= 1
        elif end_pos[1] < len(matrix[end_pos[0]]) - 1 and matrix[end_pos[0]][end_pos[1] + 1] == pos - 1:
            end_pos[1] = end_pos[1]+1
            way.append([end_pos[0], end_pos[1]])
            pos -= 1


    for position in way:
        labyrinth[position[0]][position[1]] = '$'
    return labyrinth




print(print_labyrinth(find_exit(labyrinth,[2,0],[0,3])))
    