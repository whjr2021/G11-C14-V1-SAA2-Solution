# Define the class Family
class Family:
    # Define the __init__ method with object properties- firstname, lastname, age, relation
    def __init__(self, firstname, lastname, age, relation):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.relation = relation
    
    # Define a method full_name to print firstname concatenated with last name
    def full_name(self):
       print(self.firstname + " " + self.lastname)

# Create the objects father, mother, sister and brother
father = Family("Bob", "Smith", 23, "father")
mother = Family("Amanda", "Smith", 23, "mother")
sister = Family("Jen", "Smith", 17, "sister")
brother = Family("Ben", "Smith", 18, "brother")

# Print the full names of each family member
father.full_name()
mother.full_name()
sister.full_name()
brother.full_name()