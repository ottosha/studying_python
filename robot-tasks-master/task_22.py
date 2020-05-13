#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():

    while wall_is_beneath() is False:
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
        if not wall_is_beneath():
            fill_cell()
            move_down()
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
        if not wall_is_beneath():
            fill_cell()
            move_down()
    while wall_is_on_the_right() is False:
        fill_cell()
        move_right()
    fill_cell()
    while wall_is_on_the_left() is False:
        move_left()



if __name__ == '__main__':
    run_tasks()
