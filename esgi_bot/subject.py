class Subject(object):
    name = teacher = ""
    coeff = ects = 0
    marks = []

    def __init__(self, name, teacher, coeff, ects, marks):
        self.name = name
        self.teacher = teacher
        self.coeff = coeff
        self.ects = ects
        self.marks = marks

    def __str__(self):
        return "name: {}\n" \
               "teacher: {}\n" \
               "coeff: {}\n" \
               "ects: {}\n" \
               "marks: {}".format(self.name, self.teacher, self.coeff, self.ects, self.marks)
