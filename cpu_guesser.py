import argparse
import time
import utils
from itertools import product


def product_guess(passwd_type, length):
    '''
    Generate a list of all combinations from given length then find
    the password in the list
    :param passwd_type: the types of characters in the password
    :param length: the length of the password
    :return None
    '''
    func = utils.SWITCHER.get(passwd_type)
    passwd = func(length)
    print(f"Password is: {passwd}")
    guess = None

    start = time.time()
    guesses = list(product(utils.TYPE_DICT[passwd_type], repeat=length))
    end = time.time()
    print(f"Time taken to generate permutations: {end - start} seconds.")

    guesses = [''.join(guess) for guess in guesses]

    start = time.time()
    # We loop through here to simulate guessing instead of just using list.index()
    for i, guess in enumerate(guesses):
        if guess == passwd:
            break
        else:
            continue
    end = time.time()
    
    print(f"Guessed password is {guess}")
    print(f"Made {i} 'guesses' in {end - start} seconds.")

def integer_product(passwd_type, length):
    '''
    Function to test cartesian product speeds with integers for
    comparison with PyTorch cartesian product since PyTorch tensors
    do not support chars or strings
    :param passwd_type: the types of characters in the password
    :param length: the length of the password
    :return None
    '''
    chars = utils.TYPE_DICT[passwd_type]
    idx_list = list(range(0, len(chars)))

    start = time.time()
    list(product(idx_list, repeat=length))
    end = time.time()

    print(f"Time taken to generate permutations: {end - start} seconds.")

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
    parser.add_argument('passwd_type', metavar='T', help='Type of chars in password')
    parser.add_argument('length', metavar='N', type=int, help='Number of chars in password')
    args = parser.parse_args()

    # integer_product(args.passwd_type, args.length)

    start = time.time()
    product_guess(args.passwd_type, args.length)
    end = time.time()
    print(f"Total time taken to guess password: {end - start} seconds.")