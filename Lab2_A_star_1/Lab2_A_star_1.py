from A_star import *
import time

if __name__ == "__main__":
    queens = [0, 6, 3, 3, 5, 0, 4, 0]
    root = Node(queens)
    start_time = time.time()
    result = A_star(root)
    print('Time: %s seconds' % (time.time() - start_time))
    if result != None:
        print('Solution: ', result.queens)
    else:
         print('Solution was not found')
