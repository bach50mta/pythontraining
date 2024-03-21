# Câu hỏi:

# Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance


class person():
    name = 'person'
    def __init__(self, name=None):
        self.name = name

jeffrey = person("Jeffrey")
print ("%s name is %s" % (person.name, jeffrey.name))

nico = person()
nico.name = "Nico"
print ("%s name is %s" % (person.name, nico.name))
