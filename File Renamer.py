# Утилита для переименования файлов
# Автор: [Ваше имя]

import os


def main():
    print("Программа для переименования файлов")
    print("-----------------------------------")

    # Спрашиваем путь к папке
    path = input("Введите путь к папке с файлами: ").strip()

    # Убираем кавычки если есть
    path = path.strip('"').strip("'")
    # Проверяем есть ли папка
    if not os.path.exists(path):
        print("Ошибка: Папка не существует!")
        return

    if not os.path.isdir(path):
        print("Ошибка: Это не папка!")
        return

    # Получаем все файлы
    try:
        all_files = os.listdir(path)
    except PermissionError:
        print("Ошибка: Нет доступа к папке!")
        return

    files = []
    for f in all_files:
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path):
            files.append(f)

    if len(files) == 0:
        print("В этой папке нет файлов!")
        return

    print(f"Нашел {len(files)} файлов в папке")

    # Выбор способа
    print("\nКак будем переименовывать?")
    print("1 - Просто пронумеровать (001, 002...)")
    print("2 - Добавить слово в начало")
    print("3 - Заменить часть названия")

    choice = input("Выберите 1, 2 или 3: ").strip()

    # Переменные для настроек
    prefix = ""
    start_num = 1
    old_text = ""
    new_text = ""

    if choice == "1":
        prefix = input("Какое слово поставить перед цифрами? (например 'photo'): ").strip()
        if prefix == "":
            prefix = "file"
        num_start = input("С какой цифры начать? (нажмите Enter для 1): ").strip()
        if num_start != "":
            try:
                start_num = int(num_start)
            except ValueError:
                start_num = 1
                print("Не понял число, начну с 1")

    elif choice == "2":
        prefix = input("Какое слово добавить в начало? ").strip()
        if prefix == "":
            prefix = "new_"

    elif choice == "3":
        old_text = input("Какой текст заменить? ").strip()
        new_text = input("На какой текст заменить? ").strip()
        if old_text == "":
            print("Надо указать что заменять!")
            return
    else:
        print("Не понял выбор, буду нумеровать")
        choice = "1"
        prefix = "file"

    # Показываем что получится
    print("\nВот что получится:")
    print("------------------")

    file_changes = []

    for i in range(len(files)):
        old_name = files[i]
        name_part, file_ext = os.path.splitext(old_name)

        if choice == "1":
            num = start_num + i
            new_name = f"{prefix}_{num:03d}{file_ext}"
        elif choice == "2":
            new_name = prefix + old_name
        elif choice == "3":
            new_name = old_name.replace(old_text, new_text)
        else:
            new_name = f"file_{i + 1:03d}{file_ext}"

        file_changes.append((old_name, new_name))
        print(f"{old_name}  ->  {new_name}")

    # Спрашиваем подтверждение
    print(f"\nВсего файлов для переименования: {len(file_changes)}")
    confirm = input("Переименовать? (да/нет): ").strip().lower()

    if confirm not in ["да", "д", "yes", "y"]:
        print("Отмена операции")
        return

    # Переименовываем файлы
    success = 0
    errors = 0

    print("\nНачинаю переименование...")

    for old, new in file_changes:
        try:
            old_path = os.path.join(path, old)
            new_path = os.path.join(path, new)

            # Если имя не изменилось, пропускаем
            if old == new:
                print(f"Пропускаю {old} - имя не меняется")
                continue

            # Если файл с новым именем уже существует
            if os.path.exists(new_path):
                print(f"Ошибка: файл {new} уже существует!")
                errors += 1
                continue

            os.rename(old_path, new_path)
            print(f"OK: {old} -> {new}")
            success += 1

        except Exception as e:
            print(f"ОШИБКА с {old}: {str(e)}")
            errors += 1

    # Итоги
    print("\n" + "=" * 40)
    print("ВСЕ СДЕЛАНО!")
    print(f"Успешно: {success} файлов")
    print(f"Ошибок: {errors} файлов")

    if errors == 0:
        print("Все файлы переименованы успешно! 👍")
    else:
        print("Были ошибки, проверьте выше 👆")


# Запускаем программу
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем")
    except Exception as e:
        print(f"Случилась непредвиденная ошибка: {e}")
        input("Нажмите Enter для выхода...")