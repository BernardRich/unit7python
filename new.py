import random

roll = 0 
while roll< 12:
    print(random.randint(1,6), random. randint(1,6))
    roll += 1

respomses = [" Out of luck", "try again later","no","yes","most likely no","most likely yes","maybe", "your lucky day"]
user_question = input(" ask the magic 8ball ehatever you want:")

