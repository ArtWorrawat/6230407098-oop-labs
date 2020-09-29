class Student:
    def __init__(self, name, *ids):
        self.name = name
        self.ids = ids


if __name__ == '__main__':
    manee = Student("Manee", "842004")
    mana = Student("Mana", "842004", "842005", "842006")
    chujai = Student("chujai", "842004", "842006")
    print(f"{manee.name} registered courses {manee.ids}" )
    print(f"{mana.name} registered courses {mana.ids}")
    print(f"{chujai.name} registered courses {chujai.ids}")