from app.animal import Cat, Dog, Hamster, Horse, Camel, Donkey
from app.counter import Counter


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