import animals
import dog_park

# Initialize / create names for variables that will use animals' methods
#required with dunder init in animals file

burt = animals.Dog("Burt") 
ann = animals.Husky("Ann")
chippy = animals.Chihuahua("Chippy")
zorro = animals.Labrador("Zorro")
jake = animals.Cat()

dogs = [animals.Husky("Ann"),
    animals.Chihuahua("Chippy"),
    animals.Labrador("Zorro")]
park = dog_park.DogPark(dogs)

park.converse()


# burt.speak()
# burt.eat()
# burt.learn_name("Burt")
# print (burt.name)
burt.call_dog("Come here Burt")
burt.call_dog("Burt, do you want to play")
burt.call_dog("Come here dumb dog")
burt.call_dog("Burt, I have a snack")

# jake.eat()
# jake.speak()
# jake.eat()
# print (jake.scientific_name)
print (burt.scientific_name)

ann.speak()
ann.eat()
print(issubclass(bool,int))