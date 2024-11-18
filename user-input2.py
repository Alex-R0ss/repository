import random
characters = ["power","makima","himeno","reze","kobeni","asa mitaka","quanxi","halloween","yoru","fami","Akane"]
var1 = random.choice(characters)
x = input(var1 + ", smash or pass (s/p)? ")
if var1 == "asa mitaka":
    if x == "s":
        print("good job")
    if x == "p":
        print("sad")
if var1 == "makima":
    if x == "s":
        print("good job")
    if x == "p":
        print("sad")
