#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    def krest():
        move_down()
        fill_cell()
        move_down()
        move_right()
        fill_cell()
        move_up()
        fill_cell()
        move_right()
        fill_cell()
        move_up()
        move_left()
        fill_cell()
        move_left()

    for i in range(9):  #
        krest()
        move_right(4)
    krest()
    move_down(4)
    for i in range(9):  #
        krest()
        move_left(4)
    krest()
    move_down(4)
    for i in range(9):  #
        krest()
        move_right(4)
    krest()
    move_down(4)
    for i in range(9):  #
        krest()
        move_left(4)
    krest()
    move_down(4)
    for i in range(9):  #
        krest()
        move_right(4)
    krest()
    while wall_is_on_the_left() is False:
        move_left()


if __name__ == '__main__':
    run_tasks()
