
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Roman Závorka
email: romanz90zero@gmail.com
discord: romanz90
"""

import random as r

def introduction():
    print("Hi there!\n"
          f"{60*'-'}\n"
          "I've generated a random 4 digit number for you.\n"
          "Let's play a bulls and cows game.")

def number_generator(digits_count):
    digits = []
    digits += str(r.randint(1,9))
    while len(digits) != digits_count:
            rand_digit = str(r.randint(0,9))
            if rand_digit not in digits:
                digits += rand_digit
    return digits

def guess_check():
    index = 1
    while index > 0:
        print(60*"-")
        index = 0
        input_number = str(input(f"Enter a number: \n{60*'-'}\n>>> "))
        duplicity = 0
        not_numeric = 0

        for number in input_number:
            if input_number.count(number) > 1:
                index += 1
                duplicity += 1
            if number.isnumeric() != True:
                index += 1
                not_numeric += 1
        if duplicity > 0:  
            print("Number must not contain duplicities!")
        if not_numeric > 0: 
            print("Number must contain numeric letters only!")
        if len(input_number) != 4:
            index += 1
            if len(input_number) < 4:
                print("Number is too short!")
            elif len(input_number) > 4:
                print("Number is too long!")
        if input_number[0].isnumeric() == True:
            if int(input_number[0]) == 0:
                print("First digit in the number must not be 0!")
                index += 1
    return input_number

def cows(guessed_number, generated_number):
    cows = 0
    for digit in guessed_number:
        if digit in generated_number:
            cows += 1
    return cows

def bulls(guessed_number, generated_number):
    bulls = 0
    index = 0
    for digit in guessed_number:
        if digit == generated_number[index]:
            bulls += 1
        index += 1
    return bulls

def cows_sign(count):
    if count == 1:
        return f"{count} cow"
    else:
        return f"{count} cows"

def bulls_sign(count):
    if count == 1:
        return f"is {count} bull"
    else:
        return f"are {count} bulls"
    
def bulls_cows_sentence(guess_number, generated_number):
    print(f"There {bulls_sign(bulls(guess_number, generated_number))}" 
          f" and {cows_sign(cows(guess_number, generated_number))}.")

def attempts_sentence(attempt_count):
    if attempt_count == 1:
        print("Correct, you've guessed the right number\n"
              "in 1 guess!")
    else:
        print("Correct, you've guessed the right number\n"
              f"in {attempt_count} guesses!")

def attempts_counting(generated_number):
    guess = guess_check()
    attempt_count = 1
    if bulls(guess, generated_number) == 4 and cows(guess, generated_number) == 4:
        attempts_sentence (attempt_count)

    else:
        bulls_cows_sentence (guess, generated_number)
        while bulls(guess, generated_number) != 4:
            attempt_count += 1
            guess = guess_check()
            if bulls(guess, generated_number) == 4:
                  attempts_sentence (attempt_count)
            else:
                bulls_cows_sentence (guess, generated_number)
    return attempt_count

def attempts_rating(attempt_count):
    print(60*"-")
    if attempt_count == 1:
        print("That's amazing!")
    elif attempt_count <4:
        print("That's great!")
    elif attempt_count <7:
        print("That's average!")
    else:
        print("That's not so good!")

introduction()

attempts_rating(attempts_counting(number_generator(4)))