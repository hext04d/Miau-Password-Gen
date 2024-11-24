import random
import string

def randonumstr ():
    number = random.randint(100, 9999)

    digit_list = [int(digit) + 1 for digit in str(number)]

    result = ''

    for digit in digit_list:
        randomstr = random.choice(string.ascii_lowercase)
        randomstrcaps = random.choice(string.ascii_uppercase)
        randomsymb = random.choice (string.punctuation)
        result += str(digit) + randomstr + randomstrcaps + randomsymb
        
        for i in range(10):
            result = ''.join(random.sample(result, len(result)))
    return(result)

for i in range(5):
    psswrd = randonumstr()
    print('password lenght: %d' %len(psswrd))

    print ('here is the password: ' + psswrd)
