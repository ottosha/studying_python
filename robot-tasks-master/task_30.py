#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    a = 1;
    b = 1;
    while wall_is_on_the_right() is False:
        move_right()
        a+=1

    while b > 0:
        b = 0
        for i in range(1, a):
            if not i == 1 or i == (a-1):
                fill_cell()
                b+=1
            move_down()
        for i in range(1, a):
            if not i == 1 or i == a-1:
                fill_cell()
                b+=1
            move_left()
        for i in range(1, a):
            if not i == 1 or i == a-1:
                fill_cell()
                b+=1
            move_up()
        for i in range(1, a):
            if not i == 1 or i == a-1:
                fill_cell()
                b+=1
            move_right()
        a-=2
        move_down()
        move_left()
    while wall_is_beneath() is False:
        move_down()
    while wall_is_on_the_left() is False:
        move_left()


if __name__ == '__main__':
    run_tasks()
