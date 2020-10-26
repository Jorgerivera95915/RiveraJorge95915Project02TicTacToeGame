#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#My Tic Tac Game

from itertools import permutations
from graphics import *


def fetchRes():
    # producing the permutations required for winning and storing them in the array
    arrRes = []
    squence = permutations(['7', '8', '9'])
    for x in list(squence):
        aa = ''.join(x)
        arrRes.append(aa)
    squence = permutations(['6', '5', '4'])
    for x in list(squence):
        aa = ''.join(x)
        arrRes.append(aa)
    squence = permutations(['3', '2', '1'])
    for x in list(squence):
        aa = ''.join(x)
        arrRes.append(aa)
    squence = permutations(['1', '4', '7'])
    for x in list(squence):
        aa = ''.join(x)
        arrRes.append(aa)
    squence = permutations(['2', '5', '8'])
    for x in list(squence):
        aa = ''.join(x)
        arrRes.append(aa)
    squence = permutations(['3', '6', '9'])
    for x in list(squence):
        aa = ''.join(x)
        arrRes.append(aa)
    squence = permutations(['1', '5', '9'])
    for x in list(squence):
        aa = ''.join(x)
        arrRes.append(aa)
    squence = permutations(['3', '5', '7'])
    for x in list(squence):
        aa = ''.join(x)
        arrRes.append(aa)
    return arrRes


def cheking(values_clck, combinRes):
    arrPlay = []
    combi = permutations(values_clck, 3)
    # produce all of the box permutations which is cliecked by the user or plyer
    for c in list(combi):
        aa = ''.join(c)
        arrPlay.append(aa)
    # comparing all of the winning and player permutations
    for x in arrPlay:
        if (x in combinRes):
            # if the produced permutation matches the winning permutation, it will return true
            return True


def main():
    # producing the permutations required for winning and storing them in the array
    combin_Res = fetchRes()
    # defining the screen for the game
    gameScr = GraphWin('My Tic Tac', 300, 350)  # Declaration for title and windows measurement
    gameScr.setBackground('white')
    # declaration for horizontle_lines
    st_line = Line(Point(10, 100), Point(280, 100))
    st_line.setWidth(3)
    st_line.draw(gameScr)
    st_line = Line(Point(10, 190), Point(280, 190))
    st_line.setWidth(3)
    st_line.draw(gameScr)
    # declaration for verticle_lines
    st_line = Line(Point(100, 10), Point(100, 280))
    st_line.setWidth(3)
    st_line.draw(gameScr)
    st_line = Line(Point(190, 10), Point(190, 280))
    st_line.setWidth(3)
    st_line.draw(gameScr)

    # declaring variables
    f_Arr = []
    t_Arr = []
    cont_1 = 0
    cont_2 = 0
    x = 10
    y = 10
    i = 0
    j = 8
    ply_1 = [' ']
    ply_2 = [' ']
    ppl = "X"

    # To store the boundaries I am using while-loop
    while j >= 0:
        f_Arr.append(Point(x, y))
        t_Arr.append(Point(x + 90, y + 90))
        x = x + 90
        j = j - 1
        i = i + 1
        if (i == 3):
            x = 10
            y = y + 90
            i = 0
    clk = True
    v_num = ""
    textOne = Text(Point(1, 1), ply_1)
    t2 = Text(Point(1, 1), ply_1)
    res_Fin = False
    count = 1
    box_In = False
    ptMid = Point(0, 0)

    # while_loop to fetch the co-ordinates where the player has pressed using mouse
    while count <= 9:

        check = gameScr.getMouse()

        if (check.x > f_Arr[0].x and check.x < t_Arr[0].x and check.y > f_Arr[0].y and check.y < t_Arr[0].y):
            v_num = "9"
            ptMid = Point(f_Arr[0].x + 45, f_Arr[0].y + 45)
            box_In = True
        if (check.x > f_Arr[1].x and check.x < t_Arr[1].x and check.y > f_Arr[1].y and check.y < t_Arr[1].y):
            v_num = "8"
            ptMid = Point(f_Arr[1].x + 45, f_Arr[1].y + 45)
            box_In = True
        if (check.x > f_Arr[2].x and check.x < t_Arr[2].x and check.y > f_Arr[2].y and check.y < t_Arr[2].y):
            v_num = "7"
            ptMid = Point(f_Arr[2].x + 45, f_Arr[2].y + 45)
            box_In = True
        if (check.x > f_Arr[3].x and check.x < t_Arr[3].x and check.y > f_Arr[3].y and check.y < t_Arr[3].y):
            v_num = "6"
            ptMid = Point(f_Arr[3].x + 45, f_Arr[3].y + 45)
            box_In = True
        if (check.x > f_Arr[4].x and check.x < t_Arr[4].x and check.y > f_Arr[4].y and check.y < t_Arr[4].y):
            v_num = "5"
            ptMid = Point(f_Arr[4].x + 45, f_Arr[4].y + 45)
            box_In = True
        if (check.x > f_Arr[5].x and check.x < t_Arr[5].x and check.y > f_Arr[5].y and check.y < t_Arr[5].y):
            v_num = "4"
            ptMid = Point(f_Arr[5].x + 45, f_Arr[5].y + 45)
            box_In = True
        if (check.x > f_Arr[6].x and check.x < t_Arr[6].x and check.y > f_Arr[6].y and check.y < t_Arr[6].y):
            v_num = "3"
            ptMid = Point(f_Arr[6].x + 45, f_Arr[6].y + 45)
            box_In = True
        if (check.x > f_Arr[7].x and check.x < t_Arr[7].x and check.y > f_Arr[7].y and check.y < t_Arr[7].y):
            v_num = "2"
            ptMid = Point(f_Arr[7].x + 45, f_Arr[7].y + 45)
            box_In = True
        if (check.x > f_Arr[8].x and check.x < t_Arr[8].x and check.y > f_Arr[8].y and check.y < t_Arr[8].y):
            v_num = "1"
            ptMid = Point(f_Arr[8].x + 45, f_Arr[8].y + 45)
            box_In = True
        # put point
        if box_In:
            myText = Text(ptMid, ppl)
            myText.setSize(36)
            myText.draw(gameScr)
            box_In = False
            count = count + 1
        # changing sign of the present plyer and inspecting the outcome
        if ppl == "X":
            ply_1.append(v_num)
            if len(ply_1) >= 3:
                res_Fin = cheking(ply_1, combin_Res)
            if res_Fin:
                textOne = Text(Point(gameScr.getWidth() / 2, 320), "Player " + ppl + " wins")
                textOne.setSize(20)
                textOne.setTextColor("black")
                textOne.draw(gameScr)
                clk = False
                break
            ppl = "O"
        else:
            cont_2 += 1
            ply_2.append(v_num)
            if len(ply_2) >= 3:
                res_Fin = cheking(ply_2, combin_Res)
            if res_Fin:
                textOne = Text(Point(gameScr.getWidth() / 2, 320), "Player " + ppl + " wins")
                textOne.setSize(20)
                textOne.setTextColor("black")
                textOne.draw(gameScr)
                clk = False
                break
            ppl = "X"

    # When game is drawn the text no one wins will be displayed
    if clk:
        textOne = Text(Point(gameScr.getWidth() / 2, 320), "No One wins :X")
        textOne.setSize(20)
        textOne.setTextColor("Black")
        textOne.draw(gameScr)

main() #calling main function

