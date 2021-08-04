from time import time
from typing import Callable


def run_func(callable: Callable, *args):
    t1_start = time()
    res = callable(*args)
    t1_time = time() - t1_start
    print(f"'{callable.__name__}' found result {True if res else False} in {t1_time:.02} seconds")
