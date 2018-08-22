import random

cat_food = ["bird","mouse","cat food", "dog food", "cheese"]


class Dog:
    scientific_name = "Canis lupus familiaris"
    # woof_count = 0

    def __init__(self, name):
        self.name = name
        self.woof_count = 0
        
    def speak(self):
        print("woof! "*self.woof_count)

    def eat(self):
        print("chomp, chomp, chomp")

    # replaced by dunder init statement above.  dunder init requires naming up front
    # def learn_name(self,name):
    #     self.name = name

    # def count_woof(self,woof_count):
    #     self.woof_count = self.woof_count+1

    def call_dog(self,words):
        
        if self.name in words:
            self.woof_count +=1
            self.speak()
        else:
            print("grrrrrrrr")


class Cat:
    scientific_name = "Felis catus"
    def speak(self):
        print("meow")

    def eat(self):
        self = random.choice(cat_food)
        if self == "mouse":
            print(self, "squeek!,nibble, nibble, snap, crunch")
        elif self == "bird":
            print(self,"Tweeet t t t, chirppppp, slurp, crunch, smoosh, gulp")
        else:
            print(self,"yuck!, I dont like that")


class Husky (Dog):

    def eat(self):
        print("yum, yum, yum")

    def speak(self):
        print("awoool! "*self.woof_count)

class Chihuahua (Dog):

    def eat(self):
        print("yum, yum, yum")

    def speak(self):
        print("awoool! "*self.woof_count)   

class Labrador (Dog):

    def eat(self):
        print("gulp, suck, swallow")

    def speak(self):
        print("Roof! "*self.woof_count)   