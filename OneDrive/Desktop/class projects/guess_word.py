import random


#welcome message
print("Welcome to my game")
#guess a car from a list of cars
cars = ["ferrari","Bugati","rav-4","porche"]

random_number = random.randint(0,len(cars)-1)
random_number = cars[random_number]

print(random_number)




#show the list of cars to the user
for car in cars:
    print(car)
# select the picked car
guesses = 1
picked_car = cars[2]
guess = input("Guess a car: ")
while True:
    if(picked_car == guess):
        print("You are right !")
        print(f"you tried {guesses} times")
        break
    else:
        guesses +=1
        print("Try again....")
        guess = input("guess the car")
# get the user's guess
# evaluate it
# give the result and ask to try again
