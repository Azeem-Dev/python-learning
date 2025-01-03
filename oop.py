class Student:

    # these below are class attributes/static attributes
    OldClassAttribute: str = "TEST CLASS ATTRIBUTE"
    __ClassAttribute: str = "TEST CLASS ATTRIBUTE"
    __ClassList: list[str] = ["test", "123", "456"]

    # default constructor
    def __init__(self):
        pass

    # parametarized constructor
    def __init__(self, name: str, age: int, subjects: list):  # this is the constructor method
        # self here is equvilant to this keyword
        # these below are object attributes
        self.name = name
        self.age = age
        # adding a _ _ at the start of the property makes it a private property which isn't accessible to outside scope
        self.__subjects = subjects

    # This is similar to getters in Angular
    @property
    def message(self):
        return f"Hi {self.name}, Your age is {self.age}"

    # static methods
    @staticmethod  # decorator
    def get_clsAttribute() -> str:
        return __class__.__ClassAttribute

    # class methods
    @classmethod  # decorator
    def update_clsAttribute(cls, value: str) -> None:
        cls.__ClassAttribute = value

    def get_subjects(self) -> list:  # Here -> represents return type
        return self.__subjects


newStd = Student("Azeem", 30, ["Math", "English", "Urdu"])
print(Student.OldClassAttribute)
print(newStd.name)
print(newStd.age)
print(newStd.message)
print(newStd.get_subjects())
print(Student.get_clsAttribute())

# print(newStd.__subjects())
# del newStd #This deletes/releases the memory
# print(newStd)


"""
INHERITANCE
"""


class NewStudent(Student):

    def __init__(self, name, age, subjects):
        super().__init__(name, age, subjects)

    # here _Student is the reference to the parent and then __subjects is the property in it same is the case with ClassList
    def get_concatedLists(self):
        return self._Student__subjects + self._Student__ClassList


newStdd = NewStudent("Test", 10, ["Subject tested"])
Student.update_clsAttribute("NEW CLASS ATTRIBUTE")
print(newStdd.get_clsAttribute())
print(newStdd.get_subjects())
print(newStdd.message)
print(newStdd.get_concatedLists())
