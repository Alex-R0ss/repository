import random
characters = ["kaguya","chika","miko","hayasaka","tsubame","kei","maki","moeha"]
var1 = random.choice(characters)
x = input(var1 + ", smash or pass (s/p)? ")
if var1 == "hayasaka":
    if x == "s":
        print("good job")
    if x == "p":
        print("sad")
elif var1 == "kei":
    if x == "s":
        print("good job")
    if x == "p":
        print("sad")
else:
    if x == "p":
        print("good job")
    if x == "s":
        print("sad")