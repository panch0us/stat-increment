from pathlib import Path
Path("result").mkdir(parents=True, exist_ok=True)

input_user = input("Введите символы после begin (н-р, s35): ")

def begin_title(input_user, number=0):
    begin_title = "begin " + input_user[:1] + str(int(input_user[1:]) + number)
    return begin_title

def end_title(input_user, number=0):
    end_title = "end " + input_user[:1] + str(int(input_user[1:]) + number)
    return end_title

counter_begin = 0
counter_end = 0

with open("A1F496R1.txt", "r") as file_old, open("result/A1F496R1.txt", "w+") as file_new:
    for line in file_old:
        if begin_title(input_user, counter_begin) in line:
            print(line)
            # Из строки создаем список, разбивая слова по пробелам
            line_to_list = line.split(' ')
            # Увеличиваем 2,3 значения списка на 1
            line_to_list[2] = str(int(line_to_list[2]) + 1)
            line_to_list[3] = str(int(line_to_list[3]) + 1)
            line = ' '.join(line_to_list)

            file_new.write(
                line.replace(begin_title(input_user, counter_begin), begin_title(input_user, counter_begin + 1))
            )
            counter_begin += 1
        elif end_title(input_user, counter_end) in line:
            print(line)
            file_new.write(
                line.replace(end_title(input_user, counter_end), end_title(input_user, counter_end + 1))
            )
            counter_end += 1
        else:
            file_new.write(line)