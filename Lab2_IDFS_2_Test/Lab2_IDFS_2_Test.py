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
    queens = [0, 2, 2, 1, 3, 4, 4, 3]
    print('Entry positions of queens: ', queens)
    print('The input state of the checkerboard:')
    printBoard(queens)
    root = Node(queens)
    start_time = time.time()
    result, depth, total_num_of_states, max_num_of_states_in_mem = IDFS(root)
    end_time = time.time()
    print('Solution: ', result.queens)
    print('The resulting target state of the checkerboard:')
    printBoard(result.queens)
    print('Iterations:', depth)
    print('Total number of generated states:', total_num_of_states)
    print('The maximum number of states in memory:', max_num_of_states_in_mem)
    print('Time spent: %0.5f seconds' % (end_time - start_time))
