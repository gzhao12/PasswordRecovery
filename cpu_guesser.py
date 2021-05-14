import argparse
import time
import utils
from itertools import product

def integer_product(passwd, passwd_type, length):
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

    print(f"Time taken to generate products: {end - start} seconds.")

def cartesian_prod(*chars):
    '''
    Homebrew version of calculating the cartesian product for 
    any number of sets of chars. Recursively constructs lists
    containing the cartesian products
    :param *chars: a list of characters to choose from for the
                   cartesian product
    :return a list of selected chars from the given lists
    '''
    if not chars:
        return [[]]
    else:
        return [[x] + p for x in chars[0] for p in cartesian_prod(*chars[1:])]

def product_guess(passwd, passwd_type, length):
    '''
    Generate a list of all combinations from given length then find
    the password in the list
    :param passwd_type: the types of characters in the password
    :param length: the length of the password
    :return None
    '''
    guess = None
    start = time.time()
    guesses = list(product(utils.TYPE_DICT[passwd_type], repeat=length))
    end = time.time()
    print(f"Time taken to generate products: {end - start} seconds.")

    start = time.time()
    guesses = [''.join(guess) for guess in guesses]
    end = time.time()
    print(f"Time taken to join: {end - start} seconds")

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

def homebrew_guess(passwd, passwd_type, length):
    guess = None

    chars = utils.TYPE_DICT[passwd_type]
    chars_list = [chars for i in range(0, len(passwd))]

    start = time.time()
    guesses = cartesian_prod(*chars_list)
    end = time.time()
    print(f"Time taken to generate homebrew products: {end - start} seconds.")

    start = time.time()
    guesses = [''.join(guess) for guess in guesses]
    end = time.time()
    print(f"Time taken to join: {end - start} seconds")

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('passwd_type', metavar='T', help='Type of chars in password')
    parser.add_argument('length', metavar='N', type=int, help='Number of chars in password')
    args = parser.parse_args()

    func = utils.SWITCHER.get(args.passwd_type)
    passwd = func(args.length)
    print(f"Password is: {passwd}")

    # integer_product(passwd, args.passwd_type, args.length)
    start = time.time()
    homebrew_guess(passwd, args.passwd_type, args.length)    
    end = time.time()
    print(f"Total time taken to guess password: {end - start} seconds.")

    start = time.time()
    product_guess(passwd, args.passwd_type, args.length)
    end = time.time()
    print(f"Total time taken to guess password: {end - start} seconds.")