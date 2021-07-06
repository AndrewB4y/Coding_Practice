from collections import OrderedDict as OD

n = int(input())
d = OD()
for i in range(n):
    person = input()
    person = person.split(" -")
    if person[1] in d:
        d[person[1]] += 1
    else:
        d[person[1]] = 1
od = OD(sorted(d.items(), key=lambda t: t[1]))
for i in od:
    print(i[0])

print("Algo interesante 14 yo segundo")

