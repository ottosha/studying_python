#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    pass
    if wall_is_above() & wall_is_on_the_right() &  wall_is_on_the_left():
        move_down()
    if wall_is_beneath() & wall_is_on_the_right() &  wall_is_on_the_left():
        move_up()
    if wall_is_on_the_right() & wall_is_beneath() & wall_is_above():
        move_left()
    if wall_is_on_the_left() & wall_is_beneath() & wall_is_above():
        move_right()

if __name__ == '__main__':
    run_tasks()
