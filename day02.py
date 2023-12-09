import sys
import re
import numpy as np

file = 'yay'
try:
    file = open("day2.txt", "r")
except OSError:
    print("Could not open/read file:" +  file)
    sys.exit()


#part 1

num_game = ''
max_green = 13
max_blue = 14
max_red = 12
num_added_valid_games = 0

keywords_green = ["green"]
keywords_red = ["red"]
keywords_blue = ["blue"]

def game_num():
    global num_game, max_blue, max_green, max_red, num_added_valid_games
    for line in file:
        words = re.split('; |, |: | |\n',line)
        for i in range(3, len(words), 2):
            if words[i] == 'green':
                if int(words[i - 1]) > max_green:
                    words[1] = 0
                    break
            elif words[i] == 'red':
                if int(words[i - 1]) > max_red:
                    words[1] = 0
                    break
            elif words[i] == 'blue':
                if int(words[i - 1]) > max_blue:
                    words[1] = 0
                    break
        num_game = words[1]  
        num_added_valid_games = num_added_valid_games + int(num_game)
    print('response ' + str(num_added_valid_games))
#game_num()

#part2

max_green = 0
max_blue = 0
max_red = 0
num_added_valid_games = 0

keywords_green = ["green"]
keywords_red = ["red"]
keywords_blue = ["blue"]

def game_num2():
    global num_game, max_blue, max_green, max_red, num_added_valid_games
    for line in file:
        words = re.split('; |, |: | |\n',line)
        for i in range(3, len(words), 2):
            if words[i] == 'green':
                if int(words[i - 1]) > max_green:
                    max_green = int(words[i - 1])
            elif words[i] == 'red':
                if int(words[i - 1]) > max_red:
                    max_red = int(words[i - 1])
            elif words[i] == 'blue':
                if int(words[i - 1]) > max_blue:
                    max_blue = int(words[i - 1])
        print(str(max_blue) + ' blue ' + str(max_green) + ' green ' + str(max_red) + ' red')
        num_added_valid_games = num_added_valid_games + (max_red * max_blue * max_green)
        max_green = 0
        max_blue = 0
        max_red = 0
    print('response ' + str(num_added_valid_games))


game_num2()
