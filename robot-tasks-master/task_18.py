#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while wall_is_on_the_right() is False:
        move_right()
    while wall_is_on_the_left() is False:
        if not wall_is_above():
            while not wall_is_above():
                move_up()
        move_left()

    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
