#print("www")

a=2
#print(a)
b=3
print("a/b=",int(a/b))

print(r"1000\n1000*5")
#a="kokkokok"
#b="????????"
#print(a+b)
#print(a*5)

word="123456789"
print(word[2],word[3])

#記憶體空間
a="?"
b="?"
print(a is b)
print(id(a) , id(b))
b="!"
print(id(a) , id(b))

#陣列
aa=[1,2,3,"456"]
print(id(aa))
aa[3]=4
print(id(aa))
aa.append(aa)
print(aa[4])
#################### call by value  vs  call by reference
#################### bb=aa[:]    vs      bb=aa
bb=aa
print(bb is aa)
print(chr(98)*100)
