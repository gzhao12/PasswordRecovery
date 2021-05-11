import argparse
from itertools import permutations
from project.cpu_guesser import gen_rand_lower_string, gen_rand_mix_string
import numpy as np
import sys
import string
import time
import torch

sys.path.append('../')
from cpu_guesser import (LOWERCASE, MIXCASE, ALPHANUM, SPECIAL,
                        gen_rand_lower_string, gen_rand_mix_string,
                        gen_gen_rand_mix_string, gen_rand_special_string)

def torch_guess(passwd_type, length):
    idx_list = list(range(0, len(passwd_type)))
    chars_dict = {k: v for k,v in enumerate(passwd_type)}

    tensor_a = torch.tensor(idx_list)
    tensor_b = tensor_c = tensor_d = tensor_a

    permutations = torch.cartesian_prod(tensor_a, tensor_b, tensor_c, tensor_d)

    permutations = permutations.numpy()
    permutations = permutations.astype(object)
    sort_idx = np.argsort(list(chars_dict.keys()))
    idx = np.searchsorted(list(chars_dict.keys()), permutations, sorter=sort_idx)
    out = np.asarray(list(chars_dict.values()))[sort_idx][idx]

    for i, arr in enumerate(out):
        arr = ''.join(arr)
        print(arr)


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
    torch_guess(ptype_dict[args.passwd_type], args.length)
    end = time.time()
    print(f"Total time taken to guess password: {end - start} seconds.")