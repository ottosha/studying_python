#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():

    a = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            a += 1
        if cell_is_filled() is False:
            a = 0
        if a == 3:
            break
        move_right()


if __name__ == '__main__':
    run_tasks()
