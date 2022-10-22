from IDFS import *
import time

def printBoard(queens: list):
    print('┌───┬───┬───┬───┬───┬───┬───┬───┐')
    for i in range(8):
        print('│' + '   │' * queens[i] + ' * │' + '   │' * (7 - queens[i]))
        if i != 7:
            print('├───┼───┼───┼───┼───┼───┼───┼───┤')
        else:
            print('└───┴───┴───┴───┴───┴───┴───┴───┘')


if __name__ == "__main__":
    queens = [0, 6, 3, 3, 5, 0, 4, 0]
    print('Entry positions of queens: ', queens)
    print('The input state of the checkerboard:')
    printBoard(queens)
    root = Node(queens)
    start_time = time.time()
    result, depth = IDFS(root)
    end_time = time.time()
    print('Solution: ', result.queens)
    print('The resulting target state of the checkerboard:')
    printBoard(result.queens)
    print('Iterations:', depth)
    print('Time spent: %0.5f seconds' % (end_time - start_time))
