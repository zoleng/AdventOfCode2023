file = ""
linesArray = ""

def readAndMakearray():
    global file, linesArray
    file = open("day04-testFile.txt")
    linesArray = file.readlines()

#part 1

final_count = 0
count = 0
num_point_multi = 0
num_count_final = 0

def counterMatchAndCalculRes(line):
    global final_count, count, num_count_final, num_point_multi
    num_point_multi = 0
    one_go = [name.strip() for name in line.split(':')[1].split('|')]
    one_go_new = []
    for i in one_go:
        j = i.replace('  ',' ')
        one_go_new.append(j)
    list_one = list(one_go_new[0].split(" "))
    list_two = list(one_go_new[1].split(" "))
    matches = list(set(list_one).intersection(list_two))
    for i in range(0, len(matches), 1):
        if i == 0:
            num_count_final = 1
        else:
            num_count_final = num_count_final * 2
    final_count = final_count + num_count_final
    print("finale count " + str(final_count))
    num_count_final = 0

def part1():
    global final_count
    for line in file:
      counterMatchAndCalculRes(line)

    print("""\
    ,-.       _,---._     
    /  )    .-'       `. _____
    (  (   ,'            `   /|
    \  `-"            \ \   / |
    `.              ,  \ \ /  |
    /`.          ,'-`----Y    |
    (            ;        |   '
    |  ,-.    ,-'         |  /
    |  | (   |            | /
    )  |  \  `.___________|/
    `--'   `--'

                        """)
    print("Final result : " + str(final_count))

#part1()

#part 2


#ajouter a cahnque ligne une carte nb carte, et a chaque tour ajouter a ce chiffre le nb de fois qu'on repete
def part2():
    global final_count, count, num_count_final, num_point_multi, linesArray, file
    num_card_each_card = 0
    for num_line in range(0, len(linesArray), 1):
   # for num_line, line in len(linesArray):
        one_go = [name.strip() for name in linesArray[num_line].split(':')[1].split('|')]
        one_go_new = []
        for i in one_go:
            j = i.replace('  ',' ')
            one_go_new.append(j)
        one_go_new.append(0)
        list_one = list(one_go_new[0].split(" "))
        list_two = list(one_go_new[1].split(" "))
        matches = list(set(list_one).intersection(list_two))
        print(len(matches))
        for i in range(0, len(matches), 1):
            
            num_line_to_read = int(num_line) + int(i) + int(1)
            new_line = linesArray[num_line_to_read]
            print(new_line + " new_line")
            counterMatchAndCalculRes(new_line)# send la ligne d'apres du coup changer le for
    print("""\
    ,-.       _,---._     
    /  )    .-'       `. _____
    (  (   ,'            `   /|
    \  `-"            \ \   / |
    `.              ,  \ \ /  |
    /`.          ,'-`----Y    |
    (            ;        |   '
    |  ,-.    ,-'         |  /
    |  | (   |            | /
    )  |  \  `.___________|/
    `--'   `--'

                        """)
    print("Final result : " + str(final_count))

readAndMakearray()
part2()
