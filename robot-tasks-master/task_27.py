#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    a = 1
    while wall_is_on_the_right() is False:
        fill_cell()
        for i in range(a):
            if not wall_is_on_the_right():
                move_right()
        a += 1


if __name__ == '__main__':
    run_tasks()
