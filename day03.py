
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
                num = ""
                num1 = ""
                num2 = ""
                together = False
                if arr[i - 1][j].isdigit():
                  num = arr[i - 1][j]
                  together = True
                pos = True
                neg = True
                for x in range(1, len(arr[j]), 1): 
                 #   print(arr[i + 1][j + x])
                    if arr[i - 1][j + x].isdigit() and pos == True:
                        num2 = num2 + arr[i - 1][j + x]
                    if arr[i - 1][j + x].isdigit() == False:
                        pos = False
                    if arr[i - 1][j - x].isdigit() == False:
                        neg = False
                    if arr[i - 1][j - x].isdigit() and neg == True:
                        num1 = arr[i - 1][j - x] + num1
                        neg = True
                    if pos == False and neg == False:
                        break
                if together:
                    num = num1 + num + num2
                    print(num)
                    if num != "":
                        final_num += int(num)
                else:
                    if num1 != "":
                        final_num += int(num1)
                    if num2 != "":
                        final_num += int(num2)
                    print(num1)
                    print(num2)
                num = ""
                num1 = ""
                num2 = ""
                together = False
                if arr[i + 1][j].isdigit():
                  num = arr[i + 1][j]
                  together = True
                pos = True
                neg = True
                for x in range(1, len(arr[j]), 1): 
                 #   print(arr[i + 1][j + x])
                    if arr[i + 1][j + x].isdigit() and pos == True:
                        num2 = num2 + arr[i + 1][j + x]
                    if arr[i + 1][j + x].isdigit() == False:
                        pos = False
                    if arr[i + 1][j - x].isdigit() == False:
                        neg = False
                    if arr[i + 1][j - x].isdigit() and neg == True:
                        num1 = arr[i + 1][j - x] + num1
                        neg = True
                    if pos == False and neg == False:
                        break
                if together:
                    num = num1 + num + num2
                    print(num)
                    if num != "":
                        final_num += int(num)
                else:
                    if num1 != "":
                        final_num += int(num1)
                    if num2 != "":
                        final_num += int(num2)
                    print(num1)
                    print(num2)
                num = ""
                num1 = ""
                num2 = ""
                together = False
                pos = True
                neg = True
                for x in range(1, len(arr[j]), 1): 
                 #   print(arr[i + 1][j + x])
                    if arr[i][j + x].isdigit() and pos == True:
                        num2 = num2 + arr[i][j + x]
                    if arr[i][j + x].isdigit() == False:
                        pos = False
                    if arr[i][j - x].isdigit() == False:
                        neg = False
                    if arr[i][j - x].isdigit() and neg == True:
                        num1 = arr[i][j - x] + num1
                        neg = True
                    if pos == False and neg == False:
                        break
                if num1 != "":
                    final_num += int(num1)
                if num2 != "":
                    final_num += int(num2)
                print(num1)
                print(num2)
    print(final_num)
                


readOpen()
solverPart1()
