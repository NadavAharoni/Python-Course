s1 = { "a", "b", "c", "a"}
s2 = s1
print(s1)
print(s2)

# we will now show that `add` modifies
# the set, it does not create a new one
s1.add("d")
print(s1)
print(s2)

# === compare with strings ===
str1 = "abc"
str2 = str1
print(str1)
print(str2)
print(s1 is s2)

# unlike set.add, appending to a string with +=
# creates a new string, because the original string
# is immutable
str1 += "d"
print(str1)
print(str2)


