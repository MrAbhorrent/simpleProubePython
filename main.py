HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход из программы
"""

tasks = []
today = []
tomorrow = []
other = []

run = True
while run:
    command = input("Введите комманду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print("Список задач:")
        print("Сегодня:")
        print(today)
        print("Завтра:")
        print(tomorrow)
        print("Без срока:")
        print(other)
    elif command == "add":
        timeTask = input("Дата выполенния задачи")
        task = input("Введите название задачи")
        if timeTask == "сегодня":
            today.append(task)
        elif timeTask == "завтра":
            tomorrow.append(task)
        else:
            other.append(task)
        print("Задача добавлена...")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")


print("Работа программы завершена")