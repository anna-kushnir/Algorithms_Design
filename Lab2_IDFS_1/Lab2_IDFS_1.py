from IDFS import *

queens = [4, 2, 6, 0, 0, 0, 6, 4]
root = Node(queens)
result = IDFS(root)
print('Solution: ', result.queens)