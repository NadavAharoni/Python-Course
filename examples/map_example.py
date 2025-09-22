l1 = [1,2,3]
l2 = [4,5,6,7]

def f(x,y):
    return x+y

def square(x):
    return x**2

# m = map(square, l2)
# for item in m:
#     print(item)

# m = map(f, l1, l2)
# for item in m:
#     print(item)

# z = zip(l1,l2)
# for c in z:
#     print(c)

l = list( map( lambda x,y : 5*y-2*x, l1, l2 ) )
for item in l:
    print(item)

print( max( l ) )
print( sum( l ) )

lm1 = lambda x : x**2
m = map( lambda x,y: x+y,
        map( lm1, l1),
        map( lm1, l2))

# 1, 4, 9
# 16, 25, 36
# 17, 29, 45
print( list(m) )

print( list( map( lambda x,y: (x,y), l1,l2)))
