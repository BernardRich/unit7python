import random

def travel():
    miles_traveled = random.randrange(30,61)
    days_spent = random.randrange(3,8)

    print("you've traveled" + str(miles_traveled) + "miles & it took" + str( days_spent) + " days")


def rest():
    health_increase = random.randrange(1,6)
    days_spent = random.randrange(2,6)

    print("you've gained +" + str(health_increase) + " health and it took" + str(days_spent) + "days")


def hunt():
    animal = 100
    days_spent = random.randrange(2,6)


    print("you've gained" + str(animal) + " lbs of food, and it took" + str(days_spent) + "days")


def help_function():
    commands = ['Travel', 'rest', 'hunt', 'status', 'help']
    print(commands)



date = ''
health = 5
food = 500
days_left = 336 
travel_distince = 2000

while days_left > 0:


travel()
rest()
hunt()
    