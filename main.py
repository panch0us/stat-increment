from pathlib import Path

def input_user() -> str:
    user_input = input("Введите символы после begin (н-р, s35): ")
    return user_input

def file_processing():
    # Считаем количество измененных блоков
    quantity_modified_blocks = 0
    with open("A1F496R1.txt") as file, open("result/A1F496R1.txt", "w") as new_file:
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
                new_file.write(line)
                quantity_modified_blocks += 1
            elif end_title in line:
                print(f"Блок end")
                print(f"Неизмененная строка: {line}", end='')
                # Из строки создаем список, разбивая слова по пробелам
                line_to_list = line.split(' ')
                line_to_list[1] = line_to_list[1][:1] + str(int(line_to_list[1][1:]) + 1)
                # Из измененного списка создаем строку
                line = ' '.join(line_to_list)
                print(f"Измененная строка: {line}")
                new_file.write(line)
            else:
                new_file.write(line)

    return quantity_modified_blocks


if __name__ == "__main__":
    # Проверяем, создана ли дирректрия result для сохранения файла после обработки
    Path("result").mkdir(parents=True, exist_ok=True)

    # Получаем ответ от пользователя
    response_user = input_user()

    begin_title = "begin " + response_user
    end_title = "end " + response_user

    quantity_modified_blocks = file_processing()
    print(f"Количество измененных блоков: {quantity_modified_blocks}")


        #print(f"begin_name: {begin_name}")
        #begin_name = line_to_list[1]
        #print(f"begin_name: {begin_name}")