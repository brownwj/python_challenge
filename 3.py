a='12345'
b=[]
for i in a:
    b.insert(-1,i)
b.sort()
b.reverse()
c=''
for i in b:
    c+=str(i)
print c
