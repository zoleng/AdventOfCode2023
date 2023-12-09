last_num = 0
first_num = 0
whole_num = 0
amIFirst = True
final_num = 0

list = {'one' : 'one1one', 'two' : 'two2two', 'three' : 'three3three',
'four' : 'four4four', 'five' : 'five5five', 'six' : 'six6six',
'seven' : 'seven7seven', 'eight' : 'eight8eight', 'nine' : 'nine9nine'}

file = open("day1.txt", "r")

#part 2
for line in file:
    for key in list.keys():
        line = line.replace(key, list[key])
    for ch in line:
        if ch.isnumeric() == True:
            if amIFirst:
                first_num = ch
                amIFirst = False
            last_num = ch
    amIFirst = True
    final_num = int((first_num + last_num)) + int(final_num)
    print(final_num)

#part 1
for line in file:
    for ch in line:
        if ch.isnumeric() == True:
            if amIFirst:
                first_num = ch
                amIFirst = False
            last_num = ch
    amIFirst = True
    final_num = int((first_num + last_num)) + int(final_num)
