import re
import itertools

file = ""
linesArray = ""
res = []
sequence = 'LRRLRRRLRRLLLRLLRRLRRLLRRRLRRLLRLRRRLRLRRLRLRRRLRLRLRRLLRLRLRRLRRRLRRRLRRRLRLRRLLLLRLLRLLRRLRRRLLLRLRRRLRLRRRLRLRRLRRRLRRRLRLRLLRRRLLRLLRLRLRLRLLRRLRRLRRRLRRLRLRLRLRLRRLRRRLLRRRLLRLLLRRRLLRRRLRRRLRRLRLRRLRLLRRLLRRLRLRLRRLRLRRLLRRRLLRRRLLRLRRRLRLRRRLRLRRRLRRRLRRLRRLRRLLRRRLRRRLLLRRRR'
value = 'AAA'
num_line = '0'
final_count = 0

def readAndMakearray():
    global file, linesArray, sequence, res
    file = open("day08.txt")
    linesArray = file.readlines()
    for lines in linesArray:
        res.append(re.findall(r"[\w']+", lines))
    sequence = [sub.replace('R', '2') for sub in sequence]
    sequence = [sub.replace('L', '1') for sub in sequence]
    findLine()
  #  print(arr)

#PART 1
#AAA = (BBB, CCC)
#parse en un array [AAA, BBB, CCC]
#L = arr[1], R = arr[2]
#loop tout la sequence de signe, si derniere value == ZZZ good, sinon je cotninue
def part1():
    global num_line, res, sequence, value, final_count
    i = 0
    for element in itertools.cycle(sequence):
        if value == 'ZZZ':
            final_count = i
            break
        value = res[int(num_line)][int(element)]
        findLine()
        i += 1
        
def findLine():
    global num_line, res
    for num in range(0, len(res), 1):
        if res[num][0] == value:
            num_line = num
            break


readAndMakearray()
part1()

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
print("Final result : " + str(final_count))
