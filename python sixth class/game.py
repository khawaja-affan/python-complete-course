import random
 
range = (1, 100)

game = {
    "secret_number" : random.randint(range[0], range[1]),
    "attempts" : 0
}
def myfunction():
    print("🎯 Number Guessing Games")
    print("guess a number " , range [0] , "to" , range [1] )
    guess = 0

    while guess not in range:
        guess = int(input("Enter your guess: "))
        game["attempts"] += 1

        if guess > game["seceret_number"]:
            print("Too high 🤷‍♂️.")
        elif guess < game["seceret_number"]:
            print("Too low 😅.")
        else:
            print("Correct!🎉🎊㊗️👏")
            print(f"You guessed the number in {game['attempts']} attempts.")
myfunction()
 # This is a sample function that prints "hello world" when called.
    