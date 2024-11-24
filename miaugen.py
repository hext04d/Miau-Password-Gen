'''
======================================================================================================================================
A simple algorithm for secure password generation.

───────────────────────────────────────
───▐▀▄───────▄▀▌───▄▄▄▄▄▄▄─────────────
───▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄──────────
──▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄────────
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄──────
▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───▄▄
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒█
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀─
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀───
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌────
─▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐─────
─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──────
──▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌──────
────▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀────────

======================================================================================================================================
'''
import random
import string

def randonumstr ():
    #Function that generates the password.
    number = random.randint(100, 9999)

    digit_list = [int(digit) + 1 for digit in str(number)] #Start of password generation, random str of numbers

    result = ''

    for digit in digit_list:
        #Adds random letters (up and lower case) and symbols to the existing str of numbers
        randomstr = random.choice(string.ascii_lowercase)
        randomstrcaps = random.choice(string.ascii_uppercase)
        randomsymb = random.choice (string.punctuation)
        result += str(digit) + randomstr + randomstrcaps + randomsymb
        
        for i in range(10):
            #Randomizes the result str 10 times to ensure it won't ever repeat somehow
            result = ''.join(random.sample(result, len(result)))
        
        if len(result) >= 16:
            #Makes sure it won't be longer than 16 digits per str
            result = ''.join([char for char in result if not char.isdigit()])
            result = result[:16] 
            
    while len(result) < 16:
        #Ensures that it is actually 16 digits, if the previous process fails to make it exactly 16 (which, it does sometimes)
        randomstr = random.choice(string.ascii_lowercase)
        randomstrcaps = random.choice(string.ascii_uppercase)
        randomsymb = random.choice(string.punctuation)
        result += randomstr + randomstrcaps + randomsymb

        result = ''.join(random.sample(result, len(result)))

        result = result[:16]
    return(result)

for i in range(5): 
    #Generates 5 passwords, shows them as well as their lenght
    psswrd = randonumstr()
    
    print('password lenght: %d' %len(psswrd))
    print ('here is the password: ' + psswrd)