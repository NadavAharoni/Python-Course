fr1 = frozenset(["a", "b", "c"])
fr2 = fr1

print(F"fr1={fr1}")
print(F"fr2={fr2}")

fr2 = fr2.union(["d"])
print(fr1)
print(fr2)
