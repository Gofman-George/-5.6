def show_field():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")

def moves():
    while True:
        move = input("Введите числа: ").split()
        x, y = move
        x = int(x)
        y = int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                if len(move) == 2:
                    print("Координаты введены успешно")
                    return x, y
                else:
                    print("Введите 2 числа")
            else:
                print("Строка занята")
        else:
            print("Введите числа в промежутке от 0 до 2")

def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        a = cord[0]
        b = cord[1]
        c = cord[2]
        if field[a[0]][a[1]] == field [b[0]][b[1]] == field[c[0]][c[1]] != " ":
            print(f"Выйграл {field[a[0]][a[1]]}!")
            return True
    return False
count = 0
field = [[" "] * 3 for i in range(3)]
while True:
    count += 1
    show_field()
    if count % 2 == 0:
        print("Ходит Нолик")
    else:
        print("Ходит Крестик")

    x, y = moves()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break