#def gg(text, *key, **mode):
    


#    return

def gg2(a):
    if a==20:
        f=2
        return f
    a+=1
    print(a)
    gg2(a)

#a=6
#k=gg2(a)
#print(k)

#max=lambda m,n:m if m>n else n
#print(max(10,3))

#k = lambda z,k:z**k
#print(k(5,6))
w=[1,2,3,4,5,6]
print(w.index(6))
print(set(w))

b = ('aaa','bbb')  #tuple
d = {"da":123}     #dictionary
print(d["da"])

a=[1,2,3]
c=[4,5,6]
zzzz=zip(a,c)
print(zzzz)
print(zip(*zzzz))