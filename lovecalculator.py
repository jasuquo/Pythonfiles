# 🚨capture user input below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


joined_names = name1 + name2 

names_lowercase = joined_names.lower()

#to check for word True love word count

t = names_lowercase.count("t")
r = names_lowercase.count("r")
u = names_lowercase.count("u")
e = names_lowercase.count("e")

true = t + r + u + e 

l = names_lowercase.count("l")
o = names_lowercase.count("o")
v = names_lowercase.count("v")
e = names_lowercase.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
    print (f"your score is  {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

 
