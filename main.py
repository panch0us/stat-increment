user_input = input("Введите символы после begin (н-р, s35): ")

begin_title = "begin " + user_input
end_title = "end " + user_input

def file_open():
    pass

def file_create():
    pass

with open("A1F496R1.txt") as file:
    for line in file:
        if begin_title in line:
            print(f"Блок begin")
            print(f"Неизмененная строка: {line}", end='')
            # Из строки создаем список, разбивая слова по пробелам
            line_to_list = line.split(' ')
            # Увеличиваем 1,2,3 значения списка на 1
            line_to_list[1] = line_to_list[1][:1] + str(int(line_to_list[1][1:]) + 1)
            line_to_list[2] = str(int(line_to_list[2]) + 1)
            line_to_list[3] = str(int(line_to_list[3]) + 1)
            # Из измененного списка создаем строку
            line = ' '.join(line_to_list)
            print(f"Измененная строка: {line}")
        if end_title in line:
            print(f"Блок end")
            print(f"Неизмененная строка: {line}", end='')
            # Из строки создаем список, разбивая слова по пробелам
            line_to_list = line.split(' ')
            line_to_list[1] = line_to_list[1][:1] + str(int(line_to_list[1][1:]) + 1)
            # Из измененного списка создаем строку
            line = ' '.join(line_to_list)
            print(f"Измененная строка: {line}")


    #print(f"begin_name: {begin_name}")
    #begin_name = line_to_list[1]
    #print(f"begin_name: {begin_name}")