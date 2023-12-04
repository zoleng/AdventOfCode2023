file = open("day04.txt", "r")

#part 1

final_count = 0
count = 0
num_point_multi = 0
num_count_final = 0
for line in file:
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
    num_count_final = 0
print("""\
 ,-.       _,---._ __  / 
 /  )    .-'       `./ /   
(  (   ,'            `/    /|
 \  `-"             \'\   / |
  `.              ,  \ \ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |         | /
  )  |  \  `.___________|/
  `--'   `--'

                    """)
print("Final result : " + str(final_count))

#part 2
