import math

lst = [1] + [0] * 5
print(lst)

x_str = str(4)
half = math.ceil(len(x_str) / 2) - 1
start = int("".join((["1"] + ["0"] * half)))

print(start)

print(2**31)

a = int("-00123")
print(a)

a = 5
l = list()
l.append([a, -a])
print(l)

set = {1,2,3,4,5,6}
l = list(set)
i = 0
while i < len(l) - 2:
  j = i + 1
  while j < len(l) - 1:
    if l[i] in set:
      set.remove(l[i])
    if l[j] in set:
      set.remove(l[j])
    for k in set:
        print(l[i], l[j], k)
    j += 1
  i += 1
    