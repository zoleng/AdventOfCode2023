import sys 
import re
import numpy as np


file = 'yey '
num = ""

arr = []
allSpeChar = ['!','#','$','%','&','(',')','*','+',',','-','/',':',';','<','=','>','?','@']
final_num = 0

def readOpen():
    with open("day3.txt", "r") as file:
        for line in file:
            arr.append(line)


##part 1

def solverPart1():
    global num, final_num
    for i in range(0, len(arr), 1):
        for j in range(0, len(arr[i]), 1):
            if arr[i][j] in allSpeChar:
                for upMidDown in range(-1, 2, 1): 
                    num = ""
                    num1 = ""
                    num2 = ""
                    together = False
                    if arr[i + upMidDown][j].isdigit():
                        num = arr[i + upMidDown][j]
                        together = True
                    pos = True
                    neg = True
                    for x in range(1, len(arr[j]), 1): 
                       # print(arr[i + upMidDown][j + x])
                        if arr[i + upMidDown][j + x].isdigit() and pos == True:
                            num2 = num2 + arr[i + upMidDown][j + x]
                        if  arr[i + upMidDown][j + x].isdigit() == False:
                            pos = False
                        if  arr[i + upMidDown][j - x].isdigit() == False:
                            neg = False
                        if  arr[i + upMidDown][j - x].isdigit() and neg == True:
                            num1 = arr[i + upMidDown][j - x] + num1
                            neg = True
                        if pos == False and neg == False:
                            break
                    if together:
                        num = num1 + num + num2
                        if num != "":
                            final_num += int(num)
                    else:
                        if num1 != "":
                            final_num += int(num1)
                        if num2 != "":
                            final_num += int(num2)
       
    print("""\
    ,-.       _,---._     
    /  )    .-'       `. _____
    (  (   ,'            `   /|
    \  `-"            \ \   / |
    `.              ,  \ \ /  |
    /`.          ,'-`---- Y   |
    (            ;        |   '
    |  ,-.    ,-'         |  /
    |  | (   |            | /
    )  |  \  `.___________|/
    `--'   `--'

                        """)
    print("Final result : " + str(final_num))
                


readOpen()
solverPart1()
