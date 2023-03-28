from datetime import datetime
import itertools

# Lists of all the possible characters to be used in the password.
LOWER = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p', 'g', 'w', 'y', 'b', 'v' 'k',
         'x', 'j', 'q', 'z']
UPPER = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V' 'K',
         'X', 'J', 'Q', 'Z']
NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CHARS = ['@', '#', '$', '%', '^', '&', '*', '(', ')']


def main():
    mode = input("Choose a mode (enter the corresponding number): \n(1) Only numbers\n(2) Numbers and letters\n(3) Numbers, letters, and special characters\n")
    
    realPass = input("Please enter your password: ")
    passLength = len(realPass) 

    now = datetime.now()
    guessPass = None

    if (mode == "1"):
        print("Current mode: Only numbers")
        guessPass = numbers(passLength)
    elif (mode == "2"):
        print("Current mode: Numbers and letters")
        guessPass = numbersLetters(passLength)
    elif (mode == "3"):
        guessPass = allChars(passLength)
        print("Current mode: Numbers, letters, and special characters")
    else:
        print("Invalid mode, please try again")
        main()
    
    count = 0
    # For loop to cycle through guesses
    if guessPass is not None:
        for x in guessPass:
            count += 1
            # Turns the guessed password from a list to a string
            currentGuess = ''.join(x)

            #This line prints the number of guesses as the program is running but it slows down the program considerably 
            #print("Number of guesses: " + str(count), end='\r')

            # If the guessed password matches the real password it
            if currentGuess == realPass:
                print("Guessed password: ")
                print(currentGuess)
                print("Number of guesses: ")
                print(count)
                time(now)
                break

    


#Mode functions
def numbers(passLength):
    guessPass = itertools.product(NUMS, repeat=passLength)
    return guessPass

def numbersLetters(passLength):
    guessPass = itertools.product(LOWER + UPPER + NUMS, repeat=passLength)
    return guessPass

def allChars(passLength):
    guessPass = itertools.product(LOWER + UPPER + NUMS + CHARS, repeat=passLength)
    return guessPass


#Time method
def time(now):
    later = datetime.now()
    diff = (later - now).total_seconds()

    print("Total time elapsed: " + str(diff))

if __name__ == "__main__":
    main()