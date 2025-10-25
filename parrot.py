class parrot:

    species = 'bird'
    def __init__(self, name, age):
        self.name = name
        self.age = age

bombinei = parrot('bombinei', 11)
lilli = parrot('lilli', 41)

print("The first parrot is a {}".format(bombinei.species))
print("The second parrot is a {}".format(lilli.species))

print("The first parrot's name is {} and it's age is {}".format(bombinei.name, bombinei.age))
print("The second parrot's name is {} and it's age is {}".format(lilli.name, lilli.age))
        