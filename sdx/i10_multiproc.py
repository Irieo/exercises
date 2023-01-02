#https://www.pythonforthelab.com/blog/differences-between-multiprocessing-windows-and-linux/

import multiprocessing
import random

def spawn(num):
    print(f'Spawned! {num}')

val = random.random()

def simple_func():
    print(val)

if __name__ == '__main__':
    for i in range(50):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        p.join()  #see differences w and w/o .join() -> these are NOT like on windows
        simple_func()