from pathlib import Path
Path("result").mkdir(parents=True, exist_ok=True)

file_title = input("Введите название файла с раширением для обработки (н-р, A23.txt): ")
word_search = input("Введите символы для изменения после begin (н-р, s32): ")

def begin_title(input_user, number=0):
    begin_title = "begin " + input_user[:1] + str(int(input_user[1:]) + number)
    return begin_title

def end_title(input_user, number=0):
    end_title = "end " + input_user[:1] + str(int(input_user[1:]) + number)
    return end_title

counter_begin = 0
counter_end = 0

try:
    with open(file_title, "r") as file_old, open("result/" + file_title, "w+") as file_new:
        for line in file_old:
            if begin_title(word_search, counter_begin) in line:
                print(f"строка до изменения:\t{line}", end='')
                # Из строки создаем список, разбивая слова по пробелам
                line_to_list = line.split(' ')
                # Увеличиваем 2,3 значения списка на 1
                line_to_list[2] = str(int(line_to_list[2]) + 1)
                line_to_list[3] = str(int(line_to_list[3]) + 1)
                line = ' '.join(line_to_list)
                line = line.replace(begin_title(word_search, counter_begin), begin_title(word_search, counter_begin + 1))
                file_new.write(line)
                counter_begin += 1
                print(f"строка после изменения:\t{line}", end='')
            elif end_title(word_search, counter_end) in line:
                print(f"строка до изменения:\t{line}", end='')
                line = line.replace(end_title(word_search, counter_end), end_title(word_search, counter_end + 1))
                file_new.write(line)
                counter_end += 1
                print(f"строка после изменения:\t{line}", end='')
            else:
                file_new.write(line)
except FileNotFoundError:
    print(f"Файл с названием '{file_title}' не найден. Возможно введено неверное название файла.\n"
          f"Файл должен находиться в одной директории с программой, а также необходимо указать расширение файла!\n")

input('Для выхода из программы нажмите enter.')