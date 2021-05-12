import random
import string

LOWERCASE = string.ascii_lowercase      # 26 chars
MIXCASE = string.ascii_letters          # 52 chars
ALPHANUM = MIXCASE + string.digits      # 62 chars
SPECIAL = ALPHANUM + string.punctuation # 94 chars


def gen_lower_string(length):
    '''
    Choose from all lowercase letters
    :param length: the length of the string to generate
    :return a randomly generated string consisting of only lowercase letters
    '''
    return ''.join(random.choice(LOWERCASE) for i in range(length))

def gen_mix_string(length):
    '''
    Choose from a mix of upper and lowercase letters 
    :param length: the length of the string to generate
    :return a randomly generated string consisting of uppercase and lowercase letters
    '''
    return ''.join(random.choice(MIXCASE) for i in range(length))

def gen_alphanum_string(length):
    '''
    Choose from a mix of uppercase, lowercase, and numbers
    :param length: the length of the string to generate
    :return a randomly generated string consisting of uppercase and lowercase letters
            and numbers
    '''
    return ''.join(random.choice(ALPHANUM) for i in range(length))

def gen_special_string(length):
    '''
    Choose from a mix of uppercase, lowercase, and special characters
    :param length: the length of the string to generate
    :return a randomly generated string consisting of uppercase and lowercase letters, 
            numbers, and special characters
    '''
    return ''.join(random.choice(SPECIAL) for i in range(length))

TYPE_DICT = {
    'LOWERCASE': LOWERCASE,
    'MIXCASE': MIXCASE,
    'ALPHANUM': ALPHANUM,
    'SPECIAL': SPECIAL,
}
SWITCHER = {
    'LOWERCASE': gen_lower_string,
    'MIXCASE': gen_mix_string,
    'ALPHANUM': gen_alphanum_string,
    'SPECIAL': gen_special_string,
}