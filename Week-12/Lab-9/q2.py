scoresS = input("Enter integers separated by spaces: ")
scoresSplit = scoresS.split(" ")
scores = [eval(x) for x in scoresSplit]

avg = sum(scores) / len(scores)
print(avg)

aboveEqual = 0
below = 0
for score in scores:
    if score >= avg:
        aboveEqual += 1
    else:
        below += 1
print(aboveEqual, "scores are above or equal to the average and", below, "are below the average")

