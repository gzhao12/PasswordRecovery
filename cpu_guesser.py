import argparse
import random
import string
import time
from itertools import product

LOWERCASE = string.ascii_lowercase      # 26 chars
MIXCASE = string.ascii_letters         # 52 chars
ALPHANUM = MIXCASE + string.digits     # 62 chars
SPECIAL = ALPHANUM + string.punctuation # 94 chars


def gen_rand_lower_string(length):
    '''
    Choose from all lowercase letters
    '''
    return ''.join(random.choice(LOWERCASE) for i in range(length))

def gen_rand_mix_string(length):
    '''
    Choose from a mix of upper and lowercase letters 
    '''
    return ''.join(random.choice(MIXCASE) for i in range(length))

def gen_alphanum_string(length):
    '''
    Choose from a mix of uppercase, lowercase, and numbers
    '''
    return ''.join(random.choice(ALPHANUM) for i in range(length))

def gen_rand_special_string(length):
    '''
    Choose from a mix of uppercase, lowercase, and special characters
    '''
    return ''.join(random.choice(SPECIAL) for i in range(length))

def product_guess(passwd_type, length):
    '''
    Generate a list of all combinations from given length then find
    the password in the list
    '''
    # TODO generate appropriate string type
    # make git stuff
    # break into utilities
    passwd = gen_rand_special_string(length)
    print(f"Password is: {passwd}")
    guess = None

    start = time.time()
    guesses = list(product(passwd_type, repeat=length))
    guesses = [''.join(guess) for guess in guesses]
    end = time.time()
    print(f"Time taken to generate list of guesses: {end - start} seconds.")

    start = time.time()
    # We loop through here to simulate guessing instead of just using list.index()
    for i, guess in enumerate(guesses):
        if guess == passwd:
            break
        else:
            continue
    end = time.time()
    
    print(f"Guessed password is {guess}")
    print(f"Made {i} guesses in {end - start} seconds.")

def increment_char(passwd_type, prev):
    idx = passwd_type.find(prev)
    if idx < len(passwd_type):
        inc = passwd_type[idx + 1]
        rollover = False
    else:
        inc = passwd_type[0]
        rollover = True
    
    return inc, rollover

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('passwd_type', metavar='PType', help='Type of chars in password')
    parser.add_argument('length', metavar='N', type=int, help='Number of chars in password')
    args = parser.parse_args()

    ptype_dict = {
        'LOWERCASE': LOWERCASE,
        'MIXCASE': MIXCASE,
        'ALPHANUM': ALPHANUM,
        'SPECIAL': SPECIAL,
    }

    start = time.time()
    product_guess(ptype_dict[args.passwd_type], args.length)
    end = time.time()
    print(f"Total time taken to guess password: {end - start} seconds.")

