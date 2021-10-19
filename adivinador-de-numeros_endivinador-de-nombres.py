import random
x=random.randrange(100)
print("benvingut al endivina numeros")
top_secret = x
user_guesses = 0
max_guesses = 900

while user_guesses < max_guesses:
    attempts_left = max_guesses - user_guesses
    guess = int(input("Guess a number: "))
    user_guesses += 1
    if guess == top_secret:
        print("Genial, has guanyat!")
        break
    if guess < top_secret:
        print("mes adalt!!!")
    if guess > top_secret:
        print ("mes abaix!!!")
        
