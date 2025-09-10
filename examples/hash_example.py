list1 = [1]
list1.append(2)
hash(list1)

str1 = "Hello"
h = hash(str1)
print(h)

str2 = "Hel" + "lo"
h = hash(str2)
print(h)

t = (1,2)
h = hash(t)
print(h)

t2 = (1,2)
h = hash(t2)
print(h)

exit()

def show_hash(v):
    h = hash( v )
    index = h % 17
    print(h, v, index)
    return index


d = { "Israel": "Jerusalem", "UK": "London" }
print(d["Israel"])
d["France"] = "Paris"
print(d["France"])

list1 = [ [] ] * 17
print(list1)

t = ("Israel", "Jerusalem")
i = show_hash( t[0] )


t = ("France", "Paris")
show_hash( t[0] )

t = ("Israel", "Jerusalem")
show_hash( t[0] )
