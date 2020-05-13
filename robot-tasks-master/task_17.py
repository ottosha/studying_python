#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while cell_is_filled() is False:
        move_up()
    if wall_is_on_the_left() is False:
        move_left()
    if cell_is_filled() is False:
        move_right(2)


if __name__ == '__main__':
    run_tasks()
