#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    move_right()
    while not wall_is_on_the_right():
        while wall_is_above() is False:
            move_up()
            fill_cell()
        while wall_is_beneath() is False:
            move_down()
        move_right()
    while wall_is_beneath():
        move_left()

if __name__ == '__main__':
    run_tasks()
