from threading import Thread
from time import sleep
from cinput import cinput
from blessed import Terminal

term = Terminal()

def printer():

    y = 0

    while True:
        sleep(0.1)
        if not y == term.height - 1:
            with term.location(x=0, y=y):
                print(y)

            y += 1
        else:
            blank = ''
            for i in range(term.height - 1):
                blank += term.clear_eol() + term.move_down()

            with term.location(x=0, y=0):
                print(blank, end='')
            
            y = 0


def inputer(term, length : int, prompt=''):

    print(term.move_xy(0, term.height), end='')

    while True:
        cinput(term, length, prompt)
        print(term.move_xy(0, term.height) + term.clear_eol(), end='')


if __name__ == '__main__':

    print(term.enter_fullscreen() + term.home(), end='')

    Thread(target=inputer, args=(term, 10, '> ')).start()
    Thread(target=printer).start()

