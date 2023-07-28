class Counter:
    def __init__(self):
        self._count = 0

    def add(self):
        self._count += 1

    def get_count(self):
        return self._count


class Animal:
    def __init__(self, animal_type, name, birth_date):
        self._id = None
        self.animal_type = animal_type
        self.name = name
        self.birth_date = birth_date
        self.commands = []

    def add_command(self, command):
        if isinstance(command, str):
            self.commands.append(command)
        elif isinstance(command, list):
            self.commands.extend(command)

    def set_id(self, animal_id):
        self._id = animal_id

    def __str__(self):
        commands_str = ', '.join(str(command) for command in self.commands)
        return f"ID: {self._id}, Имя: {self.name}, Тип: {self.animal_type}, Дата рождения: {self.birth_date}, Команды: {commands_str}"


class DomesticAnimal(Animal):
    pass


class WorkingAnimal(Animal):
    pass


class Cat(DomesticAnimal):
    pass


class Dog(DomesticAnimal):
    pass


class Hamster(DomesticAnimal):
    pass


class Horse(WorkingAnimal):
    pass


class Donkey(WorkingAnimal):
    pass


class Camel(WorkingAnimal):
    pass


class PetRegistry:
    def __init__(self):
        self._counter = Counter()
        self._animals = []

    def add_animal(self, animal_type, animal_class, name, birth_date, commands):
        if animal_type == "Домашний":
            animal = self._create_domestic_animal(animal_class, name, birth_date)
        elif animal_type == "Вьючный":
            animal = self._create_working_animal(animal_class, name, birth_date)
        else:
            raise ValueError("Некорректный ввод.")

        for command in commands:
            animal.add_command(command)

        animal.set_id(self._counter.get_count() + 1)
        self._counter.add()
        self._animals.append(animal)
        print(f"{animal_class} по имени {animal.name} добавлен(а) в реестр.")

    def list_all_animals(self):
        if len(self._animals) > 0:
            for animal in self._animals:
                print(animal)
        else:
            print('\nРеестр животных пуст')

    def list_animals_by_class(self):
        animals_by_class = {}
        for animal in self._animals:
            animals_by_class.setdefault(animal.animal_type, []).append(animal)
        return animals_by_class

    def count_animals_by_class(self):
        animals_by_class = self.list_animals_by_class()
        return {animal_type.capitalize(): len(animals) for animal_type, animals in animals_by_class.items()}

    def _create_domestic_animal(self, animal_class, name, birth_date):
        if animal_class == "Кот":
            return Cat("Домашний", name, birth_date)
        elif animal_class == "Собака":
            return Dog("Домашний", name, birth_date)
        elif animal_class == "Хомяк":
            return Hamster("Домашний", name, birth_date)
        else:
            raise ValueError("Некорректный ввод.")

    def _create_working_animal(self, animal_class, name, birth_date):
        if animal_class == "Лошадь":
            return Horse("Вьючный", name, birth_date)
        elif animal_class == "Осёл":
            return Donkey("Вьючный", name, birth_date)
        elif animal_class == "Верблюд":
            return Camel("Вьючный", name, birth_date)
        else:
            raise ValueError("Некорректный ввод.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None and len(self._animals) > 0:
            for animal in self._animals:
                if not animal._id:
                    raise ValueError("Нужно заполнить все поля перед выходом.")
        self._animals.clear()

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


if __name__ == "__main__":
    main()
