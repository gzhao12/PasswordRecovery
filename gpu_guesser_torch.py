import argparse
import numpy as np
import time
import torch
import utils


def move_to_gpu(value):
    '''
    Move the tensor to GPU
    :param value: the tensor to move onto the GPU
    :return the GPU stored tensor
    '''
    if torch.cuda.is_available():
        dev = "cuda:0"
    else:
        dev = "cpu"
    device = torch.device(dev)
    value = value.to(device)

    return value

def torch_guess(passwd_type, length):
    '''
    This function leverages PyTorch's cartesian_prod function to use
    CUDA to generate permutations of `length` number of tensors and
    then converts the permutations to strings
    :param passwd_type: the types of characters in the password
    :param length: the length of the password
    :return None
    '''
    func = utils.SWITCHER.get(passwd_type)
    passwd = func(length)
    print(f"Password is: {passwd}")
    guess = None

    start = time.time()
    chars = utils.TYPE_DICT[passwd_type]
    idx_list = list(range(0, len(chars)))

    tensor = torch.tensor(idx_list)
    tensors = [tensor for i in range(0, length)]
    tensors = [move_to_gpu(tensor) for tensor in tensors]

    start = time.time()
    permutations = torch.cartesian_prod(*tensors)
    end = time.time()

    print(f"Time taken to generate products: {end - start} seconds")

    permutations = permutations.cpu().numpy()
    permutations = permutations.astype(object)

    permutations = [''.join([chars[char] for char in seq]) for seq in permutations]

    for i, perm in enumerate(permutations):
        if perm == passwd:
            guess = perm
            break
    end = time.time()

    print(f"Guessed password is {guess}")
    print(f"Made {i} 'guesses' in {end - start} seconds.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('passwd_type', metavar='T', help='Type of chars in password')
    parser.add_argument('length', metavar='N', type=int, help='Number of chars in password')
    args = parser.parse_args()

    start = time.time()
    torch_guess(args.passwd_type, args.length)
    end = time.time()
    print(f"Total time taken to guess password: {end - start} seconds.")