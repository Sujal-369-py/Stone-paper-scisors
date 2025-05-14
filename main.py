from random import choice

def verify(s): 
    s = s.lower()
    return s == 'y'

def computer_guess(): 
    ch = ['r', 'p', 's'] 
    return choice(ch)

def main(): 
    name = input("Enter the user name : ")

    while True: 
        comp_guess = computer_guess() 
        user_guess = input("Enter (r) for rock, (p) for paper and (s) for scissor : ").lower() 

        print(f"{name}  :  {user_guess}    V/S    Computer  :  {comp_guess}")
        
        if comp_guess == user_guess: 
            print("Match has been tied.") 
        elif (user_guess == 'r' and comp_guess == 's') or \
             (user_guess == 'p' and comp_guess == 'r') or \
             (user_guess == 's' and comp_guess == 'p'): 
            print(f"Congratulations {name}, you won the match!")
        else: 
            print("Computer won the match.") 
        
        rm = input("Wanna do a rematch? (y) for yes and (n) for no : ")
        rematch = verify(rm)
        
        if not rematch:
            break

main()