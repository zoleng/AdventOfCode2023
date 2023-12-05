file = ""
linesArray = ""
final_count = 0
count = 0
num_point_multi = 0
num_count_final = 0
one_go_new = []
list_one = []
list_two = []
list_cards = []

def readAndMakearray():
    global file, linesArray, one_go_new, list_one, list_two
    file = open("day04.txt")
    linesArray = file.readlines()

    for num_line in range(0, len(linesArray), 1):
        one_go = [name.strip() for name in linesArray[num_line].split(':')[1].split('|')]
        one_go_new = []
        for i in one_go:
            j = i.replace('  ',' ')
            one_go_new.append(j)
        one_go_new[0] = list(one_go_new[0].split(" "))
        one_go_new[1] = list(one_go_new[1].split(" "))
        one_go_new.append(1)
        list_cards.append(one_go_new)

#part 1

def counterMatchAndCalculRes(line):
    global final_count, count, num_count_final, num_point_multi
    num_point_multi = 0
    one_go = [name.strip() for name in line.split(':')[1].split('|')]
    one_go_new = []
    for i in one_go:
        j = i.replace('  ',' ')
        one_go_new.append(j)
    final_count = final_count + num_count_final
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
    /`.          ,'-`---- Y   |
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
    global final_count, count, num_count_final, num_point_multi, linesArray, file, list_cards, list_one, list_two
    num_card_each_card = 0
    num_total_card = 0
    for num_line in range(0, len(linesArray), 1):
        num_total_card += 1
   # for num_line, line in len(linesArray):
        for num_card in range(int(list_cards[num_line][2])):
            next_card = num_line
            list_one = list_cards[num_line][0]
            list_two = list_cards[num_line][1]
            matches = list(set(list_one).intersection(list_two))
            num_total_card += len(matches)
            for i in range(0, len(matches), 1):
                next_card += 1
                list_cards[next_card][2] += 1
                num_line_to_read = int(num_line) + int(i) + int(1)
                new_line = linesArray[num_line_to_read]
               # counterMatchAndCalculRes(new_line)# send la ligne d'apres du coup changer le for
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
    print("Final result : " + str(num_total_card))

readAndMakearray()
part2()
