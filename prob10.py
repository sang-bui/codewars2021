

f = open("input.txt", "r")
villagers = f.read().splitlines() 
villagers.pop(len(villagers)-1)

times = {}

for i in villagers:
    times[i.split()[0].split("-")[1]] = int(i.split()[1].split(":")[0]) * 60 + int(i.split()[1].split(":")[1]) + int(i.split()[2]) * 10

food = []
for i in times:
    if times[i] < 1020:
        food.append(i)

if len(food) != 0:
    print("Villagers (", end="")
    for i in range(len(food)):
        if i != len(food) -1: 
            print(food[i] + ', ', end="")
        else:
            print(food[i], end="")
    print(") look tasty")
else:
    print("Blah, blah, blah, time to order delivery")





