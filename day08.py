import re
import itertools

file = ""
linesArray = ""
res = []
sequence = "LR"
#sequence = 'LRRLRRRLRRLLLRLLRRLRRLLRRRLRRLLRLRRRLRLRRLRLRRRLRLRLRRLLRLRLRRLRRRLRRRLRRRLRLRRLLLLRLLRLLRRLRRRLLLRLRRRLRLRRRLRLRRLRRRLRRRLRLRLLRRRLLRLLRLRLRLRLLRRLRRLRRRLRRLRLRLRLRLRRLRRRLLRRRLLRLLLRRRLLRRRLRRRLRRLRLRRLRLLRRLLRRLRLRLRRLRLRRLLRRRLLRRRLLRLRRRLRLRRRLRLRRRLRRRLRRLRRLRRLLRRRLRRRLLLRRRR'
value = 'AAA'
num_line = '0'
final_count = 0
num_line_list = []

def readAndMakearray():
    global file, linesArray, sequence, res
    file = open("day08-p2.txt")
    linesArray = file.readlines()
    for lines in linesArray:
        res.append(re.findall(r"[\w']+", lines))
    sequence = [sub.replace('R', '2') for sub in sequence]
    sequence = [sub.replace('L', '1') for sub in sequence]
    findLine()
    print(res)
    print(sequence)
  #  print(arr)

#PART 1
#AAA = (BBB, CCC)
#parse en un array [AAA, BBB, CCC]
#L = arr[1], R = arr[2]
#loop tout la sequence de signe, si derniere value == ZZZ good, sinon je continue
def part1():
    global num_line, res, sequence, value, final_count
    i = 0
    for element in itertools.cycle(sequence): #https://docs.python.org/3/library/itertools.html#itertools.cycle
        if value == 'ZZZ':
            final_count = i
            break
        value = res[int(num_line)][int(element)]
        print(value)
        findLine()
        i += 1
        
def findLine():
    global num_line, res
    for num in range(0, len(res), 1):
        if res[num][0] == value:
           # print(num_line)
            num_line = num
            break

## Part 2
#Find the minimum number of cycles that must be covered to get to the point in which from all our starting points, the respective arrival points are reached.
#Let's consider the example:
#We have two starting points: `11A, 22A`
#We reach a final point from `11A` iterating only one time over the given route, which is in 2 steps
#We reach a final point from `22A` iterating 3 times over the given route, which is in 6 steps
#The least common multiple between these two numbers is 6, which is our solution

def part2():
    num_loop_list = []
    findLinesLastChar('A')
    print(num_line_list)
    for num_values_to_loop in num_line_list:
        num_loop = part1Up('Z', num_values_to_loop)
        #print(num_loop)
        num_loop_list.append(num_loop)


def part1Up(char, num_line):
    global res, sequence, value, final_count
    i = 0
    print(char)
    print(num_line)
    for element in itertools.cycle(sequence): #https://docs.python.org/3/library/itertools.html#itertools.cycle
        print(element)
        print(value[2])
        if value[2] == char:
            final_count = i
            break
        value = res[int(num_line)][int(element)]
       # print(value)
        findLine2()
        i += 1
    return i

def findLine2():
    global num_line, res
    for num in range(0, len(res), 1):
        if res[num][0][2] == 'Z':
            print(num_line)
            num_line = num
            break

def findLinesLastChar(char):
    global num_line, res
    for num in range(0, len(res), 1):
        if res[num][0][2] == char:
            num_line = num
            num_line_list.append(num_line)


readAndMakearray()
#part1()
part2()

print("""\
    ,-.       _,---._     
    /  )    .-'       `. _____
    (  (   ,'            `   /|
    \  `-"            \ \   / |
    `.              ,  \ \ /  |
    /`.          ,'-`---- Y   |
    (            ;        |   |
    |  ,-.    ,-'         |  /
    |  | (   |            | /
    )  |  \  `.___________|/
    `--'   `--'

                        """)
print("Final result : " + str(final_count))
