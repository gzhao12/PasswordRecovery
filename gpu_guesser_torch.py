import argparse
import numpy as np
import time
import torch
import utils


def torch_guess(passwd_type, length):
    func = utils.SWITCHER.get(passwd_type)
    passwd = func(length)
    print(f"Password is: {passwd}")
    guess = None

    start = time.time()
    chars = utils.TYPE_DICT[passwd_type]
    idx_list = list(range(0, len(chars)))
    chars_dict = {k: v for k,v in enumerate(chars)}

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
        if arr == passwd:
            guess = arr
            break
    end = time.time()

    print(f"Guessed password is {guess}")
    print(f"Made {i} 'guesses' in {end - start} seconds.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('passwd_type', metavar='PType', help='Type of chars in password')
    parser.add_argument('length', metavar='N', type=int, help='Number of chars in password')
    args = parser.parse_args()

    start = time.time()
    torch_guess(args.passwd_type, args.length)
    end = time.time()
    print(f"Total time taken to guess password: {end - start} seconds.")