class dog:

    species = 'dog'
    def __init__(self, name, age, colour, temperament, behaviour):
        self.name = name
        self.age = age
        self.colour = colour
        self.temperament = temperament
        self.behaviour = behaviour

Golden_Retriever = dog('Josh', 12, 'gold', 'friendly', 'good with others')
German_Shepherd = dog('Mayson', 14, 'brown and black', 'friendly', 'loyal')

print("The first dog is a {}".format(Golden_Retriever.species))
print("The second dog is a {}".format(German_Shepherd.species))

print("The first dog's name is {}. He is {} years old, has a {} colour, {} temperament and his behaviour is {}"
      .format(Golden_Retriever.name, Golden_Retriever.age, Golden_Retriever.colour, Golden_Retriever.temperament, 
              Golden_Retriever.behaviour))
print("The first dog's name is {}. He is {} years old, has a {} colour, {} temperament and his behaviour is {}"
      .format(German_Shepherd.name, German_Shepherd.age, German_Shepherd.colour, German_Shepherd.temperament, 
              German_Shepherd.behaviour))