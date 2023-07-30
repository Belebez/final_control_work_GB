from app.pet_reg import PetRegistry


def choice_type():
    print('1. Домашнее животное\n'
          '2. Вьючное животное')
    while True:
        try:
            choice_num = int(input('\nКакой вид животного добавляете --> '))
            if choice_num == 1:
                return 'Домашний'
            elif choice_num == 2:
                return 'Вьючный'
            else:
                print('\nТакого пункта в меню нет.\n')
        except:
            print('\nНекорректный ввод, попробуйте еще раз.\n')
            raise

def choice_domestic():
    print('1. Кот\n'
          '2. Собака\n'
          '3. Хомяк')
    while True:
        try:
            choice_num = int(input('Введите номер добавляемого животного --> '))
            if choice_num == 1:
                return 'Кот'
            elif choice_num == 2:
                return 'Собака'
            elif choice_num == 3:
                return 'Хомяк'
            else:
                print('\nТакого пункта в меню нет.\n')
        except:
            print('\nНекорректный ввод, попробуйте еще раз.\n')
            raise

def choice_working():
    print('1. Лошадь\n'
          '2. Верблюд\n'
          '3. Осёл')
    while True:
        try:
            choice_num = int(input('Введите номер добавляемого животного --> '))
            if choice_num == 1:
                return 'Лошадь'
            elif choice_num == 2:
                return 'Верблюд'
            elif choice_num == 3:
                return 'Осёл'
            else:
                print('\nТакого пункта в меню нет.\n')
        except:
            print('\nНекорректный ввод, попробуйте еще раз.\n')
            raise

def print_menu():
    print('\nРеестр животных: ')
    print('\n1. Добавить животного')
    print('2. Вывести список всех животных')
    print('3. Обучить животного новой команде')
    print('4. Список животных по классу')
    print('5. Количество животных по классу')
    print()
    print('0. Выход')


def main():
    with PetRegistry() as registry:
        while True:
            print_menu()
            choice = input("\nВведите номер меню: ")

            if choice == "1":
                animal_type = choice_type()
                if animal_type == 'Домашний':
                    animal_class = choice_domestic()
                else:
                    animal_class = choice_working()
                name = input("Введите имя животного: ")
                birth_date = input("Введите дату рождения животного: ")
                commands = input("Введите команды животного: ").split(',')
                registry.add_animal(animal_type, animal_class, name, birth_date,
                                    [command.strip() for command in commands])
            elif choice == "2":
                registry.list_all_animals()
            elif choice == "3":
                registry.list_all_animals()
                animal_id = input("Введите ID животного, которого хотите обучить: ")
                animal = next((a for a in registry._animals if a._id == int(animal_id)), None)
                if animal:
                    new_commands = input("Введите новую команду для обучения: ").split(',')
                    animal.add_command([command.strip() for command in new_commands])
                    print(f"{animal.name} обучился новой команде")
                else:
                    print("Такого животного нет в реестре")
            elif choice == "4":
                animals_by_class = registry.list_animals_by_class()
                for animal_type, animals in animals_by_class.items():
                    print(f"{animal_type.capitalize()} тип животного:")
                    for animal in animals:
                        print(f"ID: {animal._id}, Имя: {animal.name}")
            elif choice == "5":
                animals_count_by_class = registry.count_animals_by_class()
                for animal_type, count in animals_count_by_class.items():
                    print(f"{animal_type.capitalize()} тип количество: {count}")
            elif choice == "0":
                print("Всего доброго.")
                break
            else:
                print("Некорректный ввод. Введите от 0-5 включительно")