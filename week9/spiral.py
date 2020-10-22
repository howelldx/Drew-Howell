diagonal = 501
# diagonal number as 5 gave a total of 101 so I hope this is right!
run, level, corner, total = 0, 1, 4, 0
# "level" controls how many numbers to skip before adding and "run" to control when to increase the level
# "corner" to countdown for run
for i in range(1, (diagonal)**2 + 1):
    if run == 0:
        total += i
        run = level
        corner -= 1
    elif run != 0:
        run -= 1
    if corner == 0:
        level += 2
        corner = 4
print(total)
