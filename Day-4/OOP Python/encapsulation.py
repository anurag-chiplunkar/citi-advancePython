# Encapsulation
class Person:
    def __init__(self, name):
        self.__name = name  # Encapsulated attribute with double underscores

    def display_name(self):
        return f"Name: {self.__name}"


# Creating an object of the Person class
person = Person("John Doe")

# print(person.name)

# # Accessing the encapsulated attribute (Not recommended)
print(person.Person__name)  # Output: John Doe

# Accessing the attribute using the method (Recommended)
# print(person.display_name())  # Output: Name: John Doe