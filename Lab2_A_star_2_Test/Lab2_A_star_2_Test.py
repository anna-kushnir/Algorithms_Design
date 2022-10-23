from A_star import *
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
    queens = [3, 0, 3, 7, 0, 6, 2, 5]
    print('Entry positions of queens: ', queens)
    print('The input state of the checkerboard:')
    printBoard(queens)
    root = Node(queens)
    start_time = time.time()
    result, iterations, total_num_of_states, max_num_of_states_in_mem = A_star(root)
    end_time = time.time()
    if result != None:
        print('Solution: ', result.queens)
        print('The resulting target state of the checkerboard:')
        printBoard(result.queens)
    else:
        print('Solution was not found')
    print('Iterations:', iterations)
    print('Total number of generated states:', total_num_of_states)
    print('The maximum number of states in memory:', max_num_of_states_in_mem)
    print('Time spent: %0.5f seconds' % (end_time - start_time))
