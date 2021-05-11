import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

gpu_guesser = """
#include <stdio.h>


"""