# Файл для общения с пользователем
import agent


def main():
    print("Привет! Я помощник по тренировкам.")

    workouts = []

    while True:
        user_input = input("\nВведите команду > ").strip()

        if not user_input:
            continue

        parts = user_input.split(" ", 1)
        command = parts[0].lower()

        if command == "exit":
            print("До свидания!")
            break

        elif command == "help":
            print("\nКоманды: add <название>, list, done <id>, help, exit")

        elif command == "add":
            if len(parts) > 1:
                print(agent.add_workout(workouts, parts[1]))
            else:
                print("Ошибка: Напишите название. Пример: add Приседания")

        elif command == "list":
            print(agent.show_workouts(workouts))

        elif command == "done":
            if len(parts) > 1:
                try:
                    w_id = int(parts[1])
                    print(agent.mark_done(workouts, w_id))
                except ValueError:
                    print("Ошибка: ID должен быть числом! Пример: done 1")
            else:
                print("Ошибка: Напишите ID. Пример: done 1")

        else:
            print("Неизвестная команда. Напишите help.")


if __name__ == "__main__":
    main()
