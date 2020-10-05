class ComEnStudent:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def __str__(self):
        return f"{self.name} has taken these courses:{self.courses}"

    def take_courses(self, *courses):
        for course in courses:
            self.courses.append(course)

class CoEStudent(ComEnStudent):
    def __init__(self, name, *courses):
        super(CoEStudent, self).__init__(name, *courses)

class DMEStudent(CoEStudent):
    def __init__(self, name, *courses):
        self.name = name
        super(CoEStudent, self).__init__(name, *courses)
        self.content = ""

    def make_content_type(self, type):
        self.content = type

    def __str__(self):
        return f"{self.name} has taken these courses:{self.courses}\n specialized in creating content type:{self.content} "


if __name__ == '__main__':
    com_students = []
    manee = CoEStudent("Manee", ["EN813701"])
    mana = DMEStudent("Mana", ["EN842004"])
    manee.take_courses("EN813702", "EN811301", "EN811302")
    mana.take_courses("EN842005")
    mana.make_content_type("Infographics")
    com_students.append(manee)
    com_students.append(mana)
    for com_student in com_students:
        com_student.take_courses("SC401206")
        print(com_student)
