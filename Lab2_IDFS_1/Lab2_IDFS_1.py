from IDFS import *
import time

if __name__ == "__main__":
    queens = [0, 6, 3, 3, 5, 0, 4, 0]
    root = Node(queens)
    start_time = time.time()
    result, depth = IDFS(root)
    print('Time: %s seconds' % (time.time() - start_time))
    print('Solution: ', result.queens)
    print('Was found at a depth of', depth)
