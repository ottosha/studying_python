#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():

        if not wall_is_on_the_right():
            while not wall_is_on_the_right():
                move_right()
        elif not wall_is_on_the_left():
            while not wall_is_on_the_left():
                move_left()

        if not wall_is_above():
            while not wall_is_above():
                move_up()
        elif not wall_is_beneath():
            while not wall_is_beneath():
                move_down()


if __name__ == '__main__':
    run_tasks()
