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