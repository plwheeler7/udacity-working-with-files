import animals

class DogPark:
    def __init__(self,dogs):
        self.dogs = dogs



    def rollcall(self):
        print("Dogs in Park:")
        for dog in self.dogs:
            print(f"A dog named {dog.name} is here")
        print()

    # Write the shout method here!
    def shout(self,words):
        print(words)
        for dog in self.dogs:
            dog.call_dog(words)

    def converse(self):
        self.rollcall()
        while True:
            words = input("Talk to doggos! ('quit' to quit) > ")
            if 'quit' in words:
                print("Bye!")
                break
            else:
                # The shout method is used here.
                self.shout(words)


# if __name__ == '__main__':
#     # dogs = [animals.Husky("Toklat"),
    #         animals.Chihuahua("Scrappy"),
    #         animals.Labrador("Barrett")]
    # park = DogPark(dogs)
    # park.converse()
