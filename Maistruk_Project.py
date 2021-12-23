global queen, counter, queens_amount

# Функция вывода шахматной доски
def chess_board_output():
    global counter, queens_amount
    x = y = 0
    counter += 1
    print('%d-ая разметка:\n' % counter)
    for x in range(queens_amount):
        for y in range(queens_amount):
            if x == queen[y]:
                print('[Q]', end='')
            else:
                print('[ ]', end='')
        print('')
    input('\n ...нажмите любую клавишу, чтобы увидеть следующую... \n')

# Функция проверки статуса ферзя(1 = в опасности, 0 = в безопасности)
def get_state(row, col):
    global queen
    i = 0
    queen_state = 0
    offset_row = offset_col = 0
    while (queen_state != 1) and i < col:
        offset_col = abs(i - col)
        offset_row = abs(queen[i] - row)
        # Проверка, находятся ли два ферзя на одной линии или на диагонали
        if queen[i] == row or offset_row == offset_col:
            queen_state = 1
        i = i + 1
    return queen_state

def position_process(value):
    global queen, queens_amount
    i = 0
    while i < queens_amount:
        if not get_state(i, value):
            queen[value] = i
            if value == 7:
                chess_board_output()
            else:
                position_process(value + 1)
        i += 1

# Основная программа
def main():
    global queen, counter, queens_amount
    queens_amount = 8   # Кол-во ферзей(для стандартной доски не больше 8)
    queen = [None] * 8  # Сохранить позицию в ряду из 8 ферзей
    counter = 0         # Общее количество решений
    print("Майстурук Илья\tКМ-92\nЗадача о 8-ми ферзях\n")
    position_process(0)

if __name__ == "__main__":
    main()